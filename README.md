# 📚 RAG-based LLM using Ollama

## 🚀 Overview

This project implements a **Retrieval-Augmented Generation (RAG)** system using local LLMs powered by Ollama.
It allows users to query documents and get **context-aware answers** using embeddings + vector search.

---

## 🧠 Features

* 🔍 Document loading & processing
* ✂️ Text chunking
* 🧬 Embedding generation
* 📦 Vector database storage
* 🤖 Query-based response generation using LLM
* 🏠 Fully local setup using Ollama

---

## 🛠️ Tech Stack

* Python
* Ollama (Local LLM)
* ChromaDB (Vector Database)
* LangChain

---

## 📂 Project Structure

```
├── populate_database.py     # Loads and stores embeddings
├── query_data.py            # Query interface
├── get_embedding_function.py
├── test_rag.py
├── requirements.txt
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```
git clone https://github.com/tanvii15/RAG-LLM-OLLAMA.git
cd RAG-LLM-OLLAMA
```

### 2️⃣ Create virtual environment

```
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 4️⃣ Run Ollama

Make sure Ollama is installed and running locally.

```
ollama run llama2
```

---

## ▶️ Usage

### Step 1: Populate database

```
python populate_database.py
```

### Step 2: Query data

```
python query_data.py
```

---

## 💡 Example Use Case

* Chat with your own documents
* Build local AI assistant
* Private knowledge base system

---

## 📈 Future Improvements

* Add web UI
* Support multiple documents
* Improve retrieval accuracy
* Deploy as API

---

## 👩‍💻 Author

Tanvi Agrawal

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!
