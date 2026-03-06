from langchain_community.embeddings import OllamaEmbeddings

def get_embedding_model():

    embeddings = OllamaEmbeddings(
        model="nomic-embed-text"
    )

    return embeddings