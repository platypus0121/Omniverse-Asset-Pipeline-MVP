# AI-Server-Factory-Omniverse-Pipeline

## 專案概述｜Project Overview

本專案模擬 AI 伺服器工廠的數位孿生環境。

透過 Python 實現 server rack 的批量生成，結合 Blender Quad Remesher 與 Omniverse Instancing ，以 USD 格式匯入 Stage，建立可即時協作的大型工廠場景。

## 核心功能｜Key Features

- **程序化資產生成**：Python 腳本自動產生多組 server rack 模型與工廠佈局
- **模型優化**：Blender Quad Remesher 進行減面，降低多邊形數量與檔案大小
- **高效實例化**：應用 Omniverse Instancing，減少記憶體占用，支援多台機櫃同時顯示，減少記憶體消耗
- **USD 格式轉換與批量匯入**：自動輸出優化後的 USD 資產並匯入 Stage

## 技術棧｜Tech Stack

- **平台**：NVIDIA Omniverse、OpenUSD
- **建模與優化**：Blender、Quad Remesher
- **程式語言**：Python（腳本自動化）
- **格式**：USD / USDA / USDC

## 目錄結構｜Directory Structure
```text
AI-Server-Factory-Omniverse-Pipeline/
├── docs/
│   └── screenshots/          # 實際操作截圖
│
├── scripts/
│   └── server_rack_array_generator.py    # 自動生成腳本
│
└── README.md