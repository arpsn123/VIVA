from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)

text = """
Retrieval Augmented Generation combines
retrieval and generation.
Embeddings convert text into vectors.
Vector databases store embeddings.
Cosine similarity measures semantic closeness.
Chunking is one of the most important
steps in a RAG pipeline.
"""

splitter = RecursiveCharacterTextSplitter(
    chunk_size=100, # larger chunk or smaller chunk
    chunk_overlap=30 #  when large documents are broken down into smaller pieces (chunks) for vector embeddings, the overlap ensures that important information is not lost or severed at the boundaries of those chunks, creates redundancy but its ok;
    # overlap preserves context near boundaries.
)

chunks = splitter.split_text(text)

for i, chunk in enumerate(chunks):

    print(f"\nChunk {i+1}")
    print(chunk)