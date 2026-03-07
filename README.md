Retrieval-Augmented Generation with Local Mistral (Ollama + LangChain)
This repository contains a Retrieval-Augmented Generation (RAG) system built with the LangChain framework, using a locally hosted Mistral model served via Ollama (no external API keys required).
​

The project demonstrates how to index your own documents into a vector database and build a question-answering/chat interface that grounds the LLM’s responses on those documents.
​

Features
Local Mistral model via Ollama (no cloud LLM usage).
​

Document ingestion and chunking pipeline.
​

Vector store creation under vector_db/ using build_index.py.
​

LangChain-based RAG chain: retrieve relevant chunks + generate answers.
​

Simple application entrypoint under app/ (RAG query/chat interface).
​

Project Structure
text
RETRIVAL-AUGMENTED-GENERATION/
├── app/                 # Application code (RAG chain, UI / API)
├── vector_db/           # Persisted vector database
├── build_index.py       # Script to build the index from raw docs
├── requirements.txt     # Python dependencies
├── LICENSE              # MIT License
└── RETRIVAL...docx      # Project write-up / notes
RAG Workflow Diagram (Mermaid)
You can view this diagram directly on GitHub; it shows the end-to-end flow from raw documents to RAG responses.

text
flowchart LR
    subgraph Setup["Setup & Indexing"]
        A[Raw Documents\n(PDF/TXT/Docs)] --> B[Document Loader\n(LangChain)]
        B --> C[Text Splitter\n(chunking)]
        C --> D[Embedding Model]
        D --> E[Vector Store\n(vector_db/)]
    end

    subgraph Runtime["RAG Inference"]
        F[User Query] --> G[Retriever\n(Top-k search)]
        E --> G
        G --> H[LangChain RAG Chain\n(LLM + Prompt)]
        H --> I[Local Mistral LLM\nvia Ollama]
        I --> J[Grounded Answer\n+ Sources]
    end

    style Setup fill:#e3f2fd,stroke:#1565c0
    style Runtime fill:#e8f5e9,stroke:#2e7d32
How It Works
Indexing phase (build_index.py)

Loads your local documents from a configured directory.

Splits them into chunks using LangChain text splitters.

Computes embeddings and stores them in a vector database under vector_db/.
​

Runtime (inside app/)

Starts the RAG app (CLI/REST/UI depending on your implementation).

For each user question, retrieves the most relevant chunks from vector_db/.

Sends those chunks plus the question to the local Mistral model via LangChain.

Returns a grounded answer, optionally with cited sources.
​

Prerequisites
Python (version matching requirements.txt).
​

Ollama installed and running locally.

Mistral model pulled into Ollama, for example:

bash
ollama pull mistral
Installation
Clone the repository

bash
git clone https://github.com/ARAVINDH-1505/RETRIVAL-AUGMENTED-GENERATION.git
cd RETRIVAL-AUGMENTED-GENERATION
Create and activate a virtual environment (recommended)

bash
python -m venv .venv
source .venv/bin/activate      # On Windows: .venv\Scripts\activate
Install dependencies

bash
pip install -r requirements.txt
Configure Local Mistral with Ollama
Ensure the Ollama server is running:

bash
ollama serve
By default, the code expects a model like "mistral" exposed by Ollama.
If you changed the model name or added a custom model, update the model name in the LangChain LLM configuration inside your app/ and/or build_index.py code.
​

Example LangChain LLM snippet (conceptual):

python
from langchain_community.llms import Ollama

llm = Ollama(model="mistral")
Building the Vector Index
Run the indexing script after placing your documents in the configured folder (check build_index.py for the expected path):

bash
python build_index.py
This will: load documents, chunk them, compute embeddings, and persist the vector store under vector_db/.
​

Running the RAG Application
From the project root:

bash
python -m app
Or, if your main file inside app/ is main.py:

bash
python app/main.py
Once running, you can ask questions about the documents you indexed, and the system will answer using RAG powered by the local Mistral model.
​

Example Usage
Ask: “Summarize the main ideas in my document.”

Ask: “What are the key steps mentioned for building a RAG pipeline?”

Ask: “According to the docs, how do I configure the embeddings model?”

The system will retrieve the most relevant chunks from vector_db/ and generate an answer grounded in your data.
​

Customization Ideas
Swap the embedding model (e.g., OpenAI, local embeddings via sentence-transformers).

Change the retriever strategy (top-k, MMR, etc.).

Add a Streamlit or Gradio UI on top of app/.

Log queries and retrieved documents for debugging and evaluation.
