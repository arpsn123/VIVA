from pathlib import Path

from langchain_chroma import Chroma

from langchain_ollama import (
    OllamaEmbeddings
)

from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)

from langchain_core.documents import (
    Document
)

# embedding model : 
embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

#Chunker
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)


# Read files
documents = []

for file in Path(
    "data/interview_docs"
).glob("*.txt"):

    text = file.read_text(
        encoding="utf-8"
    )

    chunks = splitter.split_text(
        text
    )

    for chunk in chunks:

        documents.append(
            Document(
                page_content=chunk,
                metadata={
                    "source": file.name
                }
            )
        )