# 🤖 AI Knowledge Base Assistant (RAG Chatbot)

## 📌 Overview

This project is a **Retrieval-Augmented Generation (RAG) based AI chatbot** that answers user queries using custom uploaded documents.

It combines **semantic search (FAISS)** with a **HuggingFace LLM (FLAN-T5)** to generate accurate, context-aware responses.

---

## 🚀 Features

* 📄 Upload PDF documents dynamically
* 🧠 Semantic search using FAISS
* 🔎 Context-based retrieval system
* 🤖 Answer generation using FLAN-T5
* 🌐 FastAPI backend
* 💬 Interactive Chat UI (HTML, CSS, JS)
* 📡 REST API endpoints (`/ask`, `/upload`)
* ⚡ Real-time responses

---

## 🏗️ Architecture

```
User (UI / Postman)
        ↓
FastAPI Backend
        ↓
Retriever (FAISS)
        ↓
Relevant Document Chunks
        ↓
LLM (FLAN-T5)
        ↓
Generated Answer
```

---

## 🛠️ Tech Stack

* Python
* FastAPI
* LangChain
* FAISS
* HuggingFace Transformers
* Sentence Transformers
* HTML, CSS, JavaScript

---

## 📂 Project Structure

```
rag-knowledge-assistant/
│
├── app/
│   ├── main.py
│   ├── document_processing/
│   ├── rag/
│   │   ├── pipeline.py
│   │   ├── llm.py
│   │   ├── prompt.py
│   │   └── retriever.py
│   └── vector_db/
│
├── frontend/
│   └── index.html
│
├── tests/
├── data/
├── vector_store/
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```
git clone https://github.com/YOUR_USERNAME/rag-knowledge-assistant.git
cd rag-knowledge-assistant
```

---

### 2. Install dependencies

```
pip install -r requirements.txt
```

---

### 3. Run the backend

```
python -m uvicorn app.main:app --reload
```

---

### 4. Open API Docs

```
http://127.0.0.1:8000/docs
```

---

### 5. Run Chat UI

Open:

```
frontend/index.html
```

---

## 📡 API Endpoints

### 🔹 POST `/ask`

#### Request:

```json
{
  "query": "What is the refund policy?"
}
```

#### Response:

```json
{
  "query": "What is the refund policy?",
  "answer": "Refunds are processed within 7 days."
}
```

---

### 🔹 POST `/upload`

* Upload PDF file
* Automatically processed and stored in vector DB

---

## 🧪 Testing

```
python tests/test_loader.py
python tests/test_splitter.py
python tests/test_embeddings.py
python tests/test_retriever.py
python tests/test_rag.py
```

---

## ⚠️ Limitations

* No chat memory (stateless chatbot)
* Works best with well-structured documents
* Requires local model download (~1GB for FLAN-T5)

---

## 🚀 Future Improvements

* Add chat memory
* Improve UI (dark mode, file upload button)
* Deploy on cloud (Render / AWS)
* Use advanced LLMs (Mistral / Llama)

---

## 💼 Resume Highlight

> Built a full-stack RAG-based AI chatbot using FastAPI, FAISS, and HuggingFace FLAN-T5 model with dynamic document upload and interactive chat UI.
