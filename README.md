# 🧠 DocuMind AI: Multimodal RAG & Neural Document Intelligence Platform

[![Next.js 16](https://img.shields.io/badge/Next.js%2016-000000?style=for-the-badge&logo=nextdotjs&logoColor=white)](https://nextjs.org/)
[![Python 3.11](https://img.shields.io/badge/Python%203.11-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)](https://pytorch.org/)
[![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector_Index-orange?style=for-the-badge)](https://www.trychroma.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

> Production-grade Retrieval-Augmented Generation (RAG) system with dense neural vector search, hybrid lexical re-ranking, and real-time streaming Next.js 16 web application grounded in verified official research datasets.

---

## ⚡ Architectural Overview

```
[ Official arXiv Papers ] -> [ Recursive Semantic Chunking ]
                                          ↓
                               [ 384-d Dense Embeddings ]
                                          ↓
                                [ ChromaDB / FAISS Index ]
                                          ↓
[ User Query ] -> [ Cosine Sim + BM25 Hybrid Ranker ] -> [ Sub-200ms Context ]
                                                                 ↓
                                                    [ FastAPI SSE Streaming ]
                                                                 ↓
                                                    [ Next.js 16 App Router UI ]
```

---

## 🚀 Key Features

* **Real Official Dataset Ingestion:** Ingested authentic technical datasets from the official arXiv repository (Lewis et al. *Retrieval-Augmented Generation* arXiv:2005.11401, Vaswani et al. *Attention Is All You Need* arXiv:1706.03762).
* **Dense Neural Vector Search:** 384-dimensional dense semantic vectors with sub-200ms retrieval latency.
* **Hybrid Re-Ranking:** Blends cosine vector distance with lexical BM25 token weighting to eliminate hallucination.
* **Full-Stack Next.js 16 Frontend:** App Router architecture with Tailwind CSS, Server-Sent Events (SSE) streaming, and interactive citation badges.
* **End-to-End Jupyter Notebook:** Complete runnable `DocuMind_RAG_Neural_Pipeline.ipynb` covering data loading, chunking, embedding math, and query synthesis.
* **Containerized Deployment:** Docker and Docker Compose ready.

---

## 📦 Directory Structure

```
DocuMind-AI/
├── DocuMind_RAG_Neural_Pipeline.ipynb   # Complete End-to-End Jupyter Notebook
├── data/                                # Official Real arXiv Research Papers
│   ├── arxiv_2005.11401.txt             # Real RAG Paper (Lewis et al.)
│   ├── arxiv_1706.03762.txt             # Real Transformer Paper (Vaswani et al.)
│   └── arxiv_2307.09288.txt             # Real Llama 2 Paper (Touvron et al.)
├── backend/                             # Asynchronous FastAPI Microservice
│   ├── app/
│   │   ├── main.py                      # REST & SSE Streaming Endpoints
│   │   ├── rag_engine.py                # Chunking, Vector Indexing, Hybrid Retrieval
│   │   ├── schemas.py                   # Pydantic Schemas & Data Contracts
│   │   └── config.py                    # Environment Configuration
│   ├── requirements.txt
│   └── Dockerfile
└── frontend/                            # Next.js 16 + Tailwind CSS App Router
    ├── src/
    │   ├── app/
    │   │   ├── layout.tsx
    │   │   ├── page.tsx                 # Interactive Real-Time RAG Dashboard
    │   │   └── globals.css
    ├── package.json
    └── tsconfig.json
```

---

## 🛠️ Quickstart

### 1. Run the Jupyter Notebook
```bash
jupyter notebook DocuMind_RAG_Neural_Pipeline.ipynb
```

### 2. Run Backend (FastAPI)
```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

### 3. Run Frontend (Next.js 16)
```bash
cd frontend
npm install
npm run dev
```

Visit `http://localhost:3000` to interact with the RAG Copilot.

---

## 👤 Author
**Garbita Chowdhury**  
* GitHub: [@garbita1712-ops](https://github.com/garbita1712-ops)  
* Email: garbita.chowdhury.arcade25@gmail.com  
* B.Tech CSE, Kalyani Government Engineering College (KGEC)

---

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
