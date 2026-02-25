import React, { useState } from "react";
import "./App.css";

interface ScanResult {
  sub: string;
  domain: string;
  ip: string;
  cloud_provider: string;
  service_provider: string;
  location: string;
  country_code: string;
}

function App() {
  const [domain, setDomain] = useState("");
  const [results, setResults] = useState<ScanResult[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [execTime, setExecTime] = useState(0);

  const handleScan = async () => {
    if (!domain) return;
    setLoading(true);
    setError("");
    setResults([]);

    try {
      const response = await fetch("http://localhost:8000/api/scan/" + domain);
      if (!response.ok) throw new Error("Scan failed");
      const data = await response.json();
      setResults(data.results);
      setExecTime(data.execution_time);
    } catch (err) {
      setError("Failed to scan domain. Make sure the backend is running.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <header>
        <h1>DOMAIN ANALYZER</h1>
        <p>Advanced Cyber Intelligence & Infrastructure Mapping</p>
      </header>

      <div className="search-container">
        <div className="search-box">
          <input 
            type="text" 
            placeholder="ENTER DOMAIN..." 
            value={domain}
            onChange={(e) => setDomain(e.target.value)}
            onKeyPress={(e) => e.key === "Enter" && handleScan()}
          />
          <button onClick={handleScan} disabled={loading}>
            {loading ? "SCANNING" : "PROBE"}
          </button>
        </div>
        
        {loading && (
          <div className="scanning-loader">
            <div className="progress-bar">
              <div className="progress-inner"></div>
            </div>
          </div>
        )}
      </div>

      {error && <div className="error">{error}</div>}

      <div className="results-container">
        {results.length > 0 && (
          <div className="results-card fade-in">
            <table>
              <thead>
                <tr>
                  <th>Subdomain</th>
                  <th>Domain</th>
                  <th>IP Address</th>
                  <th>Cloud Provider</th>
                  <th>Network ISP</th>
                  <th>Location</th>
                </tr>
              </thead>
              <tbody>
                {results.map((res, index) => (
                  <tr key={index} style={{animationDelay: `${index * 0.03}s`}}>
                    <td><span className="sub">{res.sub}</span></td>
                    <td><span className="domain">{res.domain}</span></td>
                    <td><span className="ip">{res.ip}</span></td>
                    <td>
                      <span className={`provider-badge ${res.cloud_provider.toLowerCase().replace(/ /g, "-")}`}>
                        {res.cloud_provider}
                      </span>
                    </td>
                    <td><span className="service">{res.service_provider}</span></td>
                    <td className="location">
                      {res.country_code && <span className="flag">{res.country_code}</span>}
                      {res.location}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
            
            <div className="stats-footer">
              <div className="stats-item">
                Identified Hosts: <span className="stats-val">{results.length}</span>
              </div>
              <div className="stats-item">
                Execution Time: <span className="stats-val">{execTime}s</span>
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
