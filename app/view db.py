from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings

embeddings = OllamaEmbeddings(model="nomic-embed-text")

db = Chroma(
    persist_directory="vector_db",
    embedding_function=embeddings
)

collection = db._collection

count = collection.count()

print("Total chunks stored:", count)

results = collection.get(
    limit=5,
    include=["documents", "metadatas", "embeddings"]
)

for i in range(len(results["documents"])):

    print("\n--- Chunk", i+1, "---")

    print("Text:", results["documents"][i][:200])

    print("Metadata:", results["metadatas"][i])

    vector = results["embeddings"][i]

    print("Vector length:", len(vector))

    print("First 10 vector values:", vector[:10])