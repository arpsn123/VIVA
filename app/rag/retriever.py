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

# sample testing :
docs = retrieve(
    "what do u mean by vector database?"
)

for doc in docs:

    print("=" * 50)

    print(doc.metadata)

    print(doc.page_content)