from langchain_chroma import Chroma

from langchain_ollama import (
    OllamaEmbeddings
)

embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

# loading the Vector DB :
db = Chroma(
    persist_directory="data/vector_store",
    embedding_function=embeddings
)


retriever = db.as_retriever(
    search_kwargs={
        "k": 1
    }
)


def retrieve(query):
    docs = retriever.invoke(
        query
    )
    return docs
