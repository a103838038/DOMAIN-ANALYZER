# 🌑 DOMAIN ANALYZER PRO

**高階網路情報與基礎架構映射工具**

[English](./README.md) | **繁體中文**

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.11-blue.svg)
![React](https://img.shields.io/badge/react-20-blue.svg)
![Docker](https://img.shields.io/badge/docker-ready-blue.svg)

## 🚀 專案簡介

**DOMAIN ANALYZER PRO** 是一款專為網路基礎架構探測設計的高性能情資工具。它能針對網域執行深度的子網域列舉（Subdomain Enumeration），並整合即時的 **雲端供應商辨識**、**ISP 偵測** 以及 **全球地理位置追蹤**。

本專案採用前衛的 **Cyberpunk / Glassmorphism (玻璃擬態)** 視覺介面，並具備即時掃描動畫與詳細的執行效能統計。

---

## ✨ 核心功能

- 🔍 **深度子網域掃描**：整合業界標準 **SecLists Top 1,000** 常用字典庫。
- ☁️ **雲端供應商辨識**：自動識別主機是否位於 **AWS, GCP, Azure, Cloudflare 或 Akamai**。
- 📡 **網路服務商 (ISP) 偵測**：揭露每一個 IP 背後的具體電信商或網路公司。
- 🌍 **全球地理定位**：精確標示基礎架構節點所在的 **城市** 與 **國家**。
- 🚀 **高併發掃描引擎**：採用非同步並行 DNS 探測（支援 100+ 同時請求）。
- 🔋 **批次情資 API**：優化 GeoIP 獲取邏輯，使用 Batch 模式大幅降低請求頻率限制。
- 🧪 **Docker 容器化部署**：支援一鍵遷移，可在任何環境中快速啟動。
- ⏲️ **執行效能計時**：即時計算並顯示每次查詢的精確耗時。

---

## 🛠️ 技術棧

- **前端**: React (TypeScript), Vanilla CSS (玻璃擬態 UI).
- **後端**: FastAPI (Python 3.11), 非同步 DNS 解析引擎.
- **資料來源**: ip-api (Batch 模式), 雲端供應商 CIDR 映射表.
- **容器化**: Docker & Docker Compose.

---

## ⚡ 快速開始

### 方式一：Docker Compose (推薦)

請確保您的環境已安裝 [Docker](https://www.docker.com/) 與 [Docker Compose](https://docs.docker.com/compose/)。

```bash
# 1. 複製專案
git clone https://github.com/a103838038/DOMAIN-ANALYZER.git
cd DOMAIN-ANALYZER

# 2. 一鍵啟動
docker-compose up -d --build
```

啟動後，請在瀏覽器打開：**[http://localhost:4443](http://localhost:4443)**

---

### 方式二：本地開發 (Ubuntu/Linux)

#### 後端設定
```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 main.py
```

#### 前端設定
```bash
cd frontend
npm install
PORT=4443 npm start
```

---

## 🖥️ 視覺美學

介面設計採用了 **Futuristic Cyber Intelligence** 未來科技風格：
- **玻璃擬態面板**：半透明模糊質感卡片。
- **霓虹發光標籤**：針對不同雲端供應商設計的專屬配色與發光效果。
- **雷達掃描背景**：動態水平掃描線，營造即時探測氛圍。
- **JetBrains Mono 字體**：針對技術數據優化的等寬字體，提升閱讀精準度。

---

## 📜 授權條款

本專案採用 MIT 授權條款 - 詳見 LICENSE 檔案。

---

*由 ❤️ 為資安研究人員與網路工程師打造。*
