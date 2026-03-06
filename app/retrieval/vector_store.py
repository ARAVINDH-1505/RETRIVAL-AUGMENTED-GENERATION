from langchain_community.vectorstores import Chroma


def create_vector_store(chunks, embeddings):

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="vector_db"
    )

    return vector_store


def load_vector_store(embeddings):

    vector_store = Chroma(
        persist_directory="vector_db",
        embedding_function=embeddings
    )

    return vector_store