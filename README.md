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

## How It Works

This project implements a **Retrieval-Augmented Generation (RAG)** pipeline using a locally hosted Mistral model (via Ollama) and the LangChain framework.

The system will:

- Load documents
- Chunk the text
- Generate embeddings
- Save vectors to `vector_db/`
- Run the RAG application

From the project root, start the API server with:
```bash
uvicorn app.main:app --reload
```
# Example Queries
You can try queries such as:

- What is machine learning?

- What are the key steps mentioned for building an ML model?

- Explain the configuration for the model.

(These examples assume you have indexed the book Machine Learning for Absolute Beginners.)

The system will retrieve relevant document chunks and generate a context‑aware answer.

# Customization Ideas
You can extend the project by:

- Using sentence-transformers embeddings

- Adding a Streamlit UI

- Adding a Gradio chatbot interface

- Using MMR(Maximal Marginal Relevance) retrieval

- Adding query logging and evaluation

- Adding document citations

# Future Improvements
Planned enhancements include:

- Web interface

- Document highlighting

- Multi-document QA

- Evaluation metrics for RAG

- Hybrid search (BM25 + embeddings)
