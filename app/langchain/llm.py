from langchain_ollama import ChatOllama

llm = ChatOllama( 
    model="gemma4:e2b",
    temperature=0.3 # this is temparature of the LLM, higher = 1 ---> extreamly creative outputs but may hallocinate heavily, 0 = Lower ---> output becomes highly focused, deterministic, and consistent;
)
# llm object created, and reuse this LLM object in RAG, MEMORY etc;