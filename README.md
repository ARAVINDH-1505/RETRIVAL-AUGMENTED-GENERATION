# Retrieval-Augmented Generation with Local Mistral (Ollama + LangChain)

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![LangChain](https://img.shields.io/badge/LangChain-RAG-green)
![Ollama](https://img.shields.io/badge/Ollama-Local%20LLM-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

A **Retrieval-Augmented Generation (RAG)** system built with **LangChain** and a **locally hosted Mistral model via Ollama**.

This project demonstrates how to:

- Index your own documents
- Build a vector database
- Retrieve relevant document chunks
- Generate **context-grounded answers using a local LLM**

No external API keys or cloud LLM services are required.

---

# Features

- Local **Mistral LLM via Ollama**
- Document ingestion pipeline
- Automatic **text chunking**
- Vector database creation
- Retrieval-Augmented Generation (RAG)
- Grounded answers with document context
- Fully **offline capable**

---

# Project Structure
RAG
├── app/
│ ├── DATA
│ └── GENERATION
│ ├── INGESTION
│ └── RETRIEVAL
│ └── SERVICES
|
│ └── main.py
├── vector_db/
│
├── build_index.py
│
├── requirements.txt
│
├── LICENSE
│
└── README.md


---

# System Architecture

mermaid
flowchart LR

    subgraph Setup["Document Indexing"]
        A[Raw Documents\nPDF / TXT / DOCX]
        B[LangChain Document Loader]
        C[Text Splitter\nChunking]
        D[Embedding Model]
        E[Vector Store\nvector_db]

        A --> B
        B --> C
        C --> D
        D --> E
    end

    subgraph Runtime["RAG Inference"]
        F[User Query]
        G[Retriever\nTop-K Similarity Search]
        H[RAG Prompt + Context]
        I[Local Mistral LLM\nOllama]
        J[Grounded Response\n+ Sources]

        F --> G
        E --> G
        G --> H
        H --> I
        I --> J
    end

    style Setup fill:#e3f2fd,stroke:#1565c0
    style Runtime fill:#e8f5e9,stroke:#2e7d32

How It Works
1️⃣ Document Indexing

The script build_index.py performs the indexing pipeline.

Steps:

Load documents from local directory

Split documents into chunks

Generate embeddings

Store vectors in vector_db

2️⃣ Retrieval + Generation

When a user asks a question:

Query is converted into embeddings

Relevant document chunks are retrieved

Chunks + query are sent to the LLM

Mistral generates a grounded response

Prerequisites

You need:

Python 3.10+

Ollama installed

Mistral model pulled locally

Install Mistral:

ollama pull mistral

Start Ollama:

ollama serve
Installation
Clone Repository
git clone https://github.com/ARAVINDH-1505/RETRIVAL-AUGMENTED-GENERATION.git

cd RETRIVAL-AUGMENTED-GENERATION
Create Virtual Environment
Linux / Mac
python -m venv .venv

source .venv/bin/activate
Windows
python -m venv .venv

.venv\Scripts\activate
Install Dependencies
pip install -r requirements.txt
Configure LangChain with Ollama

Example configuration:

from langchain_community.llms import Ollama

llm = Ollama(model="mistral")
Build the Vector Index

Place your documents inside the configured folder and run:

python build_index.py

This will:

Load documents

Chunk the text

Generate embeddings

Save vectors to vector_db/

Run the RAG Application

From project root:

python -m app

or

python app/main.py
Example Queries
Summarize the main ideas in my document
What are the key steps mentioned for building a RAG pipeline?
Explain the configuration for the embeddings model

The system will retrieve relevant document chunks and generate a context-aware answer.

Customization Ideas

You can extend the project by:

Using sentence-transformers embeddings

Adding Streamlit UI

Adding Gradio chatbot interface

Using MMR retrieval

Adding query logging and evaluation

Adding document citations

Future Improvements

Web interface

Document highlighting

Multi-document QA

Evaluation metrics for RAG

Hybrid search (BM25 + embeddings)
