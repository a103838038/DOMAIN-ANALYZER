import dns.resolver
import ipaddress
import requests
import asyncio
import os
import time
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional, Dict

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Cloud Provider Cache
CLOUD_PROVIDERS = {
    "AWS": "https://ip-ranges.amazonaws.com/ip-ranges.json",
    "Cloudflare": "https://api.cloudflare.com/client/v4/ips",
}

ip_ranges_cache = {}
geo_cache: Dict[str, Dict] = {}

def update_ip_ranges():
    global ip_ranges_cache
    try:
        aws_data = requests.get(CLOUD_PROVIDERS["AWS"]).json()
        ip_ranges_cache["AWS"] = [ipaddress.ip_network(item["ip_prefix"]) for item in aws_data["prefixes"]]
    except: pass
    try:
        cf_data = requests.get(CLOUD_PROVIDERS["Cloudflare"]).json()
        ip_ranges_cache["Cloudflare"] = [ipaddress.ip_network(cidr) for cidr in cf_data["result"]["ipv4_cidrs"]]
    except: pass
    
    ip_ranges_cache["GCP"] = [ipaddress.ip_network("34.80.0.0/12"), ipaddress.ip_network("35.184.0.0/13")] 
    ip_ranges_cache["Azure"] = [ipaddress.ip_network("13.64.0.0/11"), ipaddress.ip_network("40.74.0.0/15")]
    ip_ranges_cache["Akamai"] = [
        ipaddress.ip_network("23.32.0.0/11"), ipaddress.ip_network("104.64.0.0/10"),
        ipaddress.ip_network("184.24.0.0/13"), ipaddress.ip_network("2.16.0.0/13"),
        ipaddress.ip_network("23.192.0.0/11"), ipaddress.ip_network("95.100.0.0/15")
    ]

def get_cloud_provider(ip_str):
    try:
        ip_obj = ipaddress.ip_address(ip_str)
        for provider, ranges in ip_ranges_cache.items():
            for network in ranges:
                if ip_obj in network:
                    return provider
    except: pass
    return "On-Premise"

async def fetch_geo_batch(ips: List[str]):
    if not ips:
        return {}
    
    results = {}
    try:
        loop = asyncio.get_event_loop()
        response = await loop.run_in_executor(None, lambda: requests.post(
            "http://ip-api.com/batch?fields=status,query,country,countryCode,city,isp,org",
            json=ips,
            timeout=5
        ))
        
        if response.status_code == 200:
            batch_data = response.json()
            for item in batch_data:
                if item.get("status") == "success":
                    ip = item.get("query")
                    city_val = item.get("city", "")
                    country_val = item.get("country", "")
                    results[ip] = {
                        "isp": item.get("isp") or item.get("org") or "Unknown ISP",
                        "location": f"{city_val}, {country_val}" if city_val and country_val else (city_val or country_val or "Unknown"),
                        "code": item.get("countryCode", "")
                    }
                    geo_cache[ip] = results[ip]
    except: pass
    return results

update_ip_ranges()

DICT_PATH = os.path.expanduser("~/domain-analyzer-pro/backend/subdomains.txt")
SUBDOMAIN_LIST = []
if os.path.exists(DICT_PATH):
    with open(DICT_PATH, "r") as f:
        SUBDOMAIN_LIST = [line.strip() for line in f.readlines() if line.strip()]

dns_semaphore = asyncio.Semaphore(100)

async def resolve_dns_only(sub: str, domain: str):
    async with dns_semaphore:
        target = domain if sub == "@" else f"{sub}.{domain}"
        try:
            loop = asyncio.get_event_loop()
            resolver = dns.resolver.Resolver()
            resolver.timeout = 1
            resolver.lifetime = 1
            answers = await loop.run_in_executor(None, lambda: resolver.resolve(target, "A"))
            return {"sub": sub, "domain": target, "ip": str(answers[0])}
        except:
            return None

@app.get("/api/scan/{domain}")
async def scan_subdomains(domain: str):
    start_time = time.time()
    
    dns_tasks = [resolve_dns_only("@", domain)]
    dns_tasks.extend([resolve_dns_only(sub, domain) for sub in SUBDOMAIN_LIST])
    
    dns_results = await asyncio.gather(*dns_tasks)
    active_hosts = [res for res in dns_results if res is not None]
    
    if not active_hosts:
        return {"results": [], "execution_time": round(time.time() - start_time, 2)}

    unique_ips = list(set(host["ip"] for host in active_hosts))
    ips_to_fetch = [ip for ip in unique_ips if ip not in geo_cache]
    
    for i in range(0, len(ips_to_fetch), 15):
        batch = ips_to_fetch[i:i+15]
        await fetch_geo_batch(batch)
        if len(ips_to_fetch) > 15:
            await asyncio.sleep(1.1)

    final_results = []
    for host in active_hosts:
        ip = host["ip"]
        info = geo_cache.get(ip, {"isp": "Unknown", "location": "Unknown", "code": ""})
        final_results.append({
            "sub": host["sub"],
            "domain": host["domain"],
            "ip": ip,
            "cloud_provider": get_cloud_provider(ip),
            "service_provider": info["isp"],
            "location": info["location"],
            "country_code": info["code"]
        })
    
    execution_time = round(time.time() - start_time, 2)
    return {"results": final_results, "execution_time": execution_time}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
