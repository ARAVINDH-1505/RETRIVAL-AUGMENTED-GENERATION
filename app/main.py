from fastapi import FastAPI
import time
from app.ingestion.embedder import get_embedding_model
from app.retrieval.vector_store import load_vector_store
from app.retrieval.retriever import get_retriever
from app.generation.llm import load_llm
from app.services.rag_pipeline import build_rag_pipeline

app = FastAPI()


embeddings = get_embedding_model()

vector_store = load_vector_store(embeddings)

retriever = get_retriever(vector_store)

llm = load_llm()

rag_chain = build_rag_pipeline(llm, retriever)


@app.get("/query")
def query(input1: str):

    start_total = time.time()

    start = time.time()
    result = rag_chain.invoke({"input": input1})
    rag_time = time.time() - start

    total_time = time.time() - start_total

    return {
        "answer": result["answer"],
        "sources": [
            {
                "page": doc.metadata.get("page"),
                "source": doc.metadata.get("source")
            }
            for doc in result["context"]
        ],
        "timing": {
            "rag_pipeline_time": rag_time,
            "total_time": total_time
        }
    }