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


results = db.similarity_search_with_score(
    "Retrieval Augmented Generation",
    k=5
)

for doc, score in results:

    print("\n")
    print(doc.metadata)
    print(score)
    print(doc.page_content[:200])


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
    "Yolo"
)

# for doc in docs:

#     print("=" * 50)

#     print(doc.metadata)

#     print(doc.page_content)