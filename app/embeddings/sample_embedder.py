from langchain_ollama import OllamaEmbeddings

embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

vector = embeddings.embed_query(
    "What is Retrieval Augmented Generation?"
)

print(type(vector))
print(len(vector))
print(vector[:10])

# this is a vector, this goes into the ChromaDB, Pinecone, Weaviate, FAISS;