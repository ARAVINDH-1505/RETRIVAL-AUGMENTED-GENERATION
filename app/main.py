import time
from fastapi import FastAPI

from app.ingestion.embedder import get_embedding_model
from app.retrieval.vector_store import load_vector_store
from app.retrieval.retriever import get_retriever
from app.generation.llm import load_llm
from app.services.rag_pipeline import build_rag_pipeline

app = FastAPI(
    title="RAG API",
    description="Retrieval Augmented Generation API using Mistral",
    version="1.0"
)

# Load components once at startup

embeddings = get_embedding_model()

vector_store = load_vector_store(embeddings)

retriever = get_retriever(vector_store)

llm = load_llm()

rag_chain = build_rag_pipeline(llm, retriever)


@app.get("/")
def home():
    return {"message": "RAG API is running"}


@app.get("/query")
def query(input1: str):

    start_time = time.time()

    result = rag_chain.invoke({"input": input1})

    latency = round(time.time() - start_time, 3)

    return {
        "answer": result["answer"],
        "sources": [
            {
                "page": doc.metadata.get("page"),
                "source": doc.metadata.get("source")
            }
            for doc in result["context"]
        ],
        "latency_seconds": latency
    }