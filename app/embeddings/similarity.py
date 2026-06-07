from langchain_ollama import OllamaEmbeddings
from sklearn.metrics.pairwise import cosine_similarity

embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

text1 = "What is machine learning?"
text2 = "Explain machine learning."
text3 = "How to cook pasta?"

vec1 = embeddings.embed_query(text1)
vec2 = embeddings.embed_query(text2)
vec3 = embeddings.embed_query(text3)

print(
    cosine_similarity([vec1], [vec2])
)

print(
    cosine_similarity([vec1], [vec3])
)