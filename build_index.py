from app.ingestion.loader import load_documents
from app.ingestion.splitter import split_documents
from app.ingestion.embedder import get_embedding_model
from app.retrieval.vector_store import create_vector_store

DATA_PATH = "app/data/documents"


def build_vector_database():

    print("Loading documents...")
    documents = load_documents(DATA_PATH)

    print("Splitting documents...")
    chunks = split_documents(documents)

    print("Loading embedding model...")
    embeddings = get_embedding_model()

    print("Creating vector store...")
    create_vector_store(chunks, embeddings)

    print("Vector database created successfully!")


if __name__ == "__main__":
    build_vector_database()