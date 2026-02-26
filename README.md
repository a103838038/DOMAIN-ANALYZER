**繁體中文** | [English](./README.md)

---

# 🌑 DOMAIN ANALYZER PRO

**Advanced Cyber Intelligence & Infrastructure Mapping Tool**

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.11-blue.svg)
![React](https://img.shields.io/badge/react-20-blue.svg)
![Docker](https://img.shields.io/badge/docker-ready-blue.svg)

## 🚀 Overview

**DOMAIN ANALYZER PRO** is a high-performance network intelligence tool designed to probe domain infrastructure. It performs deep subdomain enumeration using industry-standard dictionaries and enriches the results with real-time cloud provider detection, ISP identification, and global geo-location tracking.

Featuring a futuristic **Cyberpunk / Glassmorphism** interface with real-time scanning animations and detailed performance metrics.

---

## ✨ Key Features

- 🖧 **Name Server (NS) Scanning**: Automatically resolve domain Name Servers and fetch their IP, Cloud Provider, ISP, and Geo-Location.
- 🔍 **Deep Subdomain Enumeration**: Integrated with **SecLists Top 1,000** standard dictionary.
- ☁️ **Cloud Provider Detection**: Identify if hosts are on **AWS, GCP, Azure, Cloudflare, or Akamai**.
- 📡 **Service Provider (ISP) Identification**: Reveal the network owner for every identified IP.
- 🌍 **Global Geo-Location**: Pinpoint the city and country of infrastructure nodes.
- 🚀 **High Concurrency Engine**: Asynchronous parallel DNS probing (100+ concurrent requests).
- 🔋 **Batch Intelligence API**: Optimized GeoIP fetching using Batch API to avoid rate limits.
- 🧪 **Dockerized Deployment**: Fully containerized for instant deployment in any environment.
- ⏲️ **Performance Metrics**: Real-time execution time tracking for every scan.

---

## 🛠️ Tech Stack

- **Frontend**: React (TypeScript), Vanilla CSS (Glassmorphism UI).
- **Backend**: FastAPI (Python 3.11), Asynchronous DNS Resolver.
- **Data Sources**: ip-api (Batch Mode), Cloud Provider CIDR mappings.
- **Orchestration**: Docker & Docker Compose.

---

## ⚡ Quick Start

### Option 1: Docker Compose (Recommended)

Ensure you have [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/) installed.

```bash
# 1. Clone the repository
git clone https://github.com/a103838038/DOMAIN-ANALYZER.git
cd DOMAIN-ANALYZER

# 2. Spin up the infrastructure
docker-compose up -d --build
```

Open your browser and navigate to: **[http://localhost:4443](http://localhost:4443)**

---

### Option 2: Local Development (Ubuntu/Linux)

#### Backend Setup
```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 main.py
```

#### Frontend Setup
```bash
cd frontend
npm install
PORT=4443 npm start
```

---

## 🖥️ UI Aesthetic

The interface is built with a **Futuristic Cyber Intelligence** aesthetic, featuring:
- **Glassmorphism Panels**: Semi-transparent blurred cards.
- **Neon Glow Badges**: Specialized color-coded badges for different cloud providers.
- **Radar Scan Background**: Animated scanlines for a real-time probe feeling.
- **JetBrains Mono Typography**: Monospace fonts for precise technical data.

---

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

*Built with ❤️ for Security Researchers and Network Engineers.*
