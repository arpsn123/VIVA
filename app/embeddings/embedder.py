from langchain_ollama import OllamaEmbeddings


class EmbeddingService:

    def __init__(self):

        self.model = OllamaEmbeddings(
            model="nomic-embed-text"
        )

    def embed(self, text):

        return self.model.embed_query(
            text
        )