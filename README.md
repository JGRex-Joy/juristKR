# ⚖️ Jurist — Telegram AI Lawyer Bot (UK KR)

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.101.0-green?logo=fastapi&logoColor=white)
![Aiogram](https://img.shields.io/badge/Aiogram-3.0.0-lightgrey?logo=telegram&logoColor=white)
![Qdrant](https://img.shields.io/badge/Qdrant-1.2.0-orange?logo=qdrant&logoColor=white)
![SentenceTransformers](https://img.shields.io/badge/SentenceTransformers-2.2.0-purple?logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-24.0-blue?logo=docker&logoColor=white)


**Jurist** is an AI-powered Telegram bot that provides **reference legal assistance** based on the **Criminal Code of the Kyrgyz Republic (УК КР)**.  
The system is built on a **Retrieval-Augmented Generation (RAG)** architecture, enabling context-aware answers with references to relevant legal articles.

> ⚠️ **Disclaimer:** This project is for educational and reference purposes only and does **not** constitute legal advice.

---

## ✨ Features

- 🤖 Telegram bot interface (Aiogram)
- ⚖️ Legal Q&A based on the Criminal Code of the Kyrgyz Republic
- 🧠 RAG pipeline with:
  - Query normalization using LLM
  - Semantic search with vector embeddings
  - Context-aware answer generation
- 🔎 Vector search powered by **Qdrant**
- 📚 Article-level retrieval and explanation
- 🌍 Natural language answers (Russian-friendly embeddings)

---

## 🏗️ Architecture Overview

```
User (Telegram)
↓
Telegram Bot (Aiogram)
↓
FastAPI Backend (/ask)
↓
RAG Pipeline
├── LLM Normalizer
├── Embedder (SentenceTransformers)
├── Vector Search (Qdrant)
└── LLM Answer Generator
↓
Final Answer
```

---

## 🧩 RAG Pipeline Breakdown

### 1. Query Normalization
User input is first normalized using an LLM to reduce ambiguity and improve retrieval quality.

```
normalized_query = normalizer.normalize(user_query)
```

### 2. Embedding
The normalized query is converted into a vector using LaBSE (ru-sts) embeddings.

```
vector = embedder.encode(normalized_query)
```

### 3. Semantic Search
Relevant chunks of the Criminal Code are retrieved from Qdrant using vector similarity search.

```
context = searcher.search(vector)
```

### 4. Answer Generation
The original user question + retrieved context are passed to the LLM for answer generation.
```
answer = query.answer(user_query, context)
```

## 🧠 Models & Technologies

| Component     | Technology                                        |
|:--------------|:--------------------------------------------------|
| LLM           | Google Generative AI (`gemma-3-27b-it`)           |
| Embeddings    | `sergeyzh/LaBSE-ru-sts`                           |
| Vector DB     | Qdrant                                            |
| Chunking      | LangChain `RecursiveCharacterTextSplitter`        |
| Backend       | FastAPI                                           |
| Telegram Bot  | Aiogram                                           |

## 📂 Project Structure
```
rag_service/
├── main.py
├── data/
│   ├── uk_kr.docx
├── llm/
│   ├── client.py
│   ├── layers/
│   │   ├── base.py
│   │   ├── normalizer.py
│   │   └── query.py
├── rag/
│   ├── embedder.py
│   └── pipeline.py
├── storage/
│   ├── qdrant_store.py
│   └── qdrant_search.py
├── preprocessing/
│   ├── prepare_data.py
│   ├── docx_reader.py
│   └── chunker.py
bot/
├── main.py
```

## 🚀 Getting Started
1️⃣ Clone the repository
```
git clone https://github.com/your-username/jurist-bot.git
cd jurist-bot
```

2️⃣ Environment Variables
- Create a .env file:
```
LLM_API_KEY=your_google_genai_key
TELEGRAM_API_TOKEN=your_telegram_bot_token
BACKEND_URL=http://localhost:8000/ask
```

3️⃣ Run Qdrant
```
docker run -p 6333:6333 qdrant/qdrant
```
4️⃣ Start Backend (FastAPI)
```
uvicorn rag_service.main:app --reload
```
5️⃣ Start Telegram Bot
```
python bot/main.py
```

## 📌 API Example

### POST /ask
**Request:**
```
{
  "question": "Какая ответственность за кражу?"
}
```

**Response:**
```
{
  "answer": "Согласно статье ... УК КР, кража ..."
}
```

## 🛡️ Limitations
The bot does not replace a licensed lawyer

Answers depend on the quality of embeddings and retrieved context

Legal texts may require updates if legislation changes

## 🔮 Future Improvements
✅ Answer caching

📌 Article citation formatting

🧾 Source highlighting

🌐 Multilingual support

🔐 User session context

📊 Evaluation & retrieval metrics

## 👨‍💻 Author
JGRex-Joy - Junior AI Engineer
Built with ❤️ as a legal-tech & LLM/AI engineering project.