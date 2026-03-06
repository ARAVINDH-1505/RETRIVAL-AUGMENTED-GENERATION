from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import TextLoader
import os

def load_documents(path):

    documents = []

    for file in os.listdir(path):

        if file.endswith(".pdf"):
            loader = PyPDFLoader(os.path.join(path, file))
            documents.extend(loader.load())

        elif file.endswith(".txt"):
            loader = TextLoader(os.path.join(path, file))
            documents.extend(loader.load())

    return documents