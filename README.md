
<h1 align="center">🎙️ VIVA</h1>

<h2 align="center">
A Modular Voice AI Platform for Intelligent Technical Interviewing, Context-Aware Candidate Evaluation, and Automated Assessment
</h2>

<div align="center">
    <img src="https://img.shields.io/github/stars/arpsn123/VIVA?style=for-the-badge&logo=github&logoColor=white&color=ffca28" alt="GitHub Repo Stars">
    <img src="https://img.shields.io/github/forks/arpsn123/VIVA?style=for-the-badge&logo=github&logoColor=white&color=00aaff" alt="GitHub Forks">
    <img src="https://img.shields.io/github/watchers/arpsn123/VIVA?style=for-the-badge&logo=github&logoColor=white&color=00e676" alt="GitHub Watchers">
</div>

<div align="center">
    <img src="https://img.shields.io/github/issues/arpsn123/VIVA?style=for-the-badge&logo=github&logoColor=white&color=ea4335" alt="GitHub Issues">
    <img src="https://img.shields.io/github/issues-pr/arpsn123/VIVA?style=for-the-badge&logo=github&logoColor=white&color=ff9100" alt="GitHub Pull Requests">
</div>

<div align="center">
    <img src="https://img.shields.io/github/last-commit/arpsn123/VIVA?style=for-the-badge&logo=github&logoColor=white&color=673ab7" alt="GitHub Last Commit">
    <img src="https://img.shields.io/github/contributors/arpsn123/VIVA?style=for-the-badge&logo=github&logoColor=white&color=388e3c" alt="GitHub Contributors">
    <img src="https://img.shields.io/github/repo-size/arpsn123/VIVA?style=for-the-badge&logo=github&logoColor=white&color=303f9f" alt="GitHub Repo Size">
</div>

<div align="center">
    <img src="https://img.shields.io/github/languages/count/arpsn123/VIVA?style=for-the-badge&logo=github&logoColor=white&color=607d8b" alt="GitHub Language Count">
    <img src="https://img.shields.io/github/languages/top/arpsn123/VIVA?style=for-the-badge&logo=python&logoColor=white&color=4caf50" alt="GitHub Top Language">
</div>

<div align="center">
    <img src="https://img.shields.io/badge/AI%20Platform-Voice%20AI-6A1B9A?style=for-the-badge&logo=openai&logoColor=white">
    <img src="https://img.shields.io/badge/Status-Active%20Development-brightgreen?style=for-the-badge">
</div>

<br>

**VIVA (Voice Interview & Verification Assistant)** is an end-to-end Voice AI platform designed to simulate technical interviews through natural spoken conversations. It integrates Large Language Models (LLMs), Retrieval-Augmented Generation (RAG), Speech-to-Text (STT), and Text-to-Speech (TTS) into a unified interview pipeline capable of generating questions, evaluating responses, and delivering real-time spoken feedback.

Built around a modular architecture, each subsystem operates independently while contributing to a single conversational workflow. This design enables VIVA to remain scalable, maintainable, and easily extensible for future AI capabilities.

### Core Capabilities

* AI-generated technical interview questions
* Natural voice conversations
* Real-time Speech-to-Text (STT)
* Retrieval-Augmented Generation (RAG)
* Context-aware answer evaluation
* Adaptive interview workflow
* Text-to-Speech (TTS) feedback
* Automated interview reporting

### High-Level Architecture

```text

                  +----------------------+
                  |      Candidate       |
                  +----------+-----------+
                             |
                       Voice Response
                             |
                             ▼
                  +----------------------+
                  |   Speech-to-Text     |
                  +----------+-----------+
                             |
                             ▼
                  +----------------------+
                  |   Interview Engine   |
                  +----------+-----------+
                             |
                    +--------+--------+
                    |                 |
                    ▼                 ▼
           +---------------+   +---------------+
           | RAG Pipeline  |   |  LLM Engine   |
           +-------+-------+   +-------+-------+
                   |                   |
                   +--------+----------+
                            |
                            ▼
                  +----------------------+
                  |   Answer Evaluation  |
                  +----------+-----------+
                             |
                             ▼
                  +----------------------+
                  |   Text-to-Speech     |
                  +----------+-----------+
                             |
                       Voice Feedback
                             |
                             ▼
                  +----------------------+
                  |      Candidate       |
                  +----------------------+

```
---
VIVA | End-to-End Voice AI Technical Interview Platform Demo

https://github.com/user-attachments/assets/82d528c6-d21e-44fb-9068-34f397e3453c

*For demonstration purposes, the video has been accelerated to 3× during candidate input to keep the walkthrough concise while preserving the complete interview workflow*



---

## Technology Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

![Gemma](https://img.shields.io/badge/Gemma-4285F4?style=for-the-badge&logo=google&logoColor=white)

![Ollama](https://img.shields.io/badge/Ollama-000000?style=for-the-badge&logo=ollama&logoColor=white)

![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=chainlink&logoColor=white)

![RAG](https://img.shields.io/badge/RAG-blueviolet?style=for-the-badge)

![ChromaDB](https://img.shields.io/badge/ChromaDB-7B68EE?style=for-the-badge)

![nomic-embed-text](https://img.shields.io/badge/nomic--embed--text-FF6F00?style=for-the-badge)

![Faster-Whisper](https://img.shields.io/badge/Faster--Whisper-00A67E?style=for-the-badge)

![pyttsx3](https://img.shields.io/badge/pyttsx3-4CAF50?style=for-the-badge)

---

## LLM Engine

### Overview

The LLM Engine is the reasoning core of VIVA. It powers every intelligent interaction within the application, including interview question generation, candidate evaluation, structured feedback generation, and report synthesis.

### Model Selection

VIVA uses **Gemma4** running locally through **Ollama** as its primary language model.

### Prompt-Driven Design

Instead of embedding interview logic directly into Python code, VIVA defines model behavior through **Prompt Templates**.

This design provides:

* Better maintainability.
* Easier prompt refinement.
* Consistent model behavior.
* Clear separation between application logic and AI reasoning.

The Python application controls the workflow, while the LLM focuses solely on language understanding and reasoning.

### Current Capabilities

At this stage, the LLM Engine supports:

* Technical interview question generation.
* Context-aware answer evaluation.
* Structured JSON responses.
* Topic-specific interviews.
* Difficulty-aware prompting.
* Local inference using Ollama.

---

## Retrieval-Augmented Generation (RAG)

### Overview

The Retrieval-Augmented Generation (RAG) system is the knowledge layer of VIVA. Instead of relying solely on the internal knowledge of the Large Language Model, VIVA retrieves relevant information from a curated knowledge base and injects that context into the model before generating an evaluation.

This approach significantly improves factual grounding, reduces hallucinations, and enables the interview system to evaluate responses using domain-specific knowledge without requiring model retraining.

The RAG pipeline in VIVA is composed of six interconnected components.

```text

Retrieval-Augmented Generation

│

├── 01 LangChain

├── 02 Embeddings

├── 03 Chunking

├── 04 Vector Database

├── 05 Retrieval

└── 06 Context Injection

```

### 01. LangChain

#### Overview

LangChain serves as the orchestration layer of VIVA. It connects the application with the Large Language Model and manages the execution of AI workflows such as question generation and answer evaluation.

Instead of directly interacting with the LLM throughout the codebase, VIVA uses reusable prompts and chains to keep the implementation modular and maintainable.

#### Prompt Templates

Prompt templates define how the model should behave while keeping prompt instructions separate from the application logic.

```python

question_prompt = PromptTemplate(

    input_variables=["topic", "difficulty"],

    template=...

)

```

The same template can be reused with different topics and difficulty levels without modifying the underlying code.

#### Chains

A chain combines a prompt with the language model into a reusable pipeline.

```python

question_chain = question_prompt | llm

```

Executing the chain generates a complete interview question.

```python

result = question_chain.invoke(

    {

        "topic": topic,

        "difficulty": difficulty

    }

)

```

---

### 02. Embeddings

#### Overview

Embeddings are the foundation of semantic retrieval in VIVA. Instead of searching documents using exact keywords, both the interview documents and the user's query are converted into high-dimensional vector representations. This allows the system to retrieve information based on meaning rather than exact word matches.

#### Embedding Model

VIVA uses **`nomic-embed-text`** through Ollama to generate embeddings locally.

```python

embeddings = OllamaEmbeddings(

    model="nomic-embed-text"

)

```

Running the embedding model locally provides offline execution, zero API cost, and seamless integration with the rest of the local AI pipeline.

#### Embedding Documents

Before interview documents can be retrieved, they are converted into embeddings and stored inside the vector database.

```python

db = Chroma.from_documents(

    documents=documents,

    embedding=embeddings,

    persist_directory="data/vector_store"

)

```

Each document chunk is transformed into a numerical vector that represents its semantic meaning.

#### Embedding Queries

During an interview, the candidate's question is embedded using the same model before retrieval.

```python

retriever.invoke(query)

```

The query embedding is then compared against the stored document embeddings to identify the most relevant chunks.

---

### 03. Chunking

#### Overview

Large Language Models cannot efficiently process entire documents at once due to context window limitations. To address this, VIVA divides each knowledge base document into smaller overlapping chunks before generating embeddings.

This ensures that only the most relevant portions of a document are retrieved during evaluation.

#### Recursive Character Text Splitter

VIVA uses LangChain's `RecursiveCharacterTextSplitter` to split documents while preserving as much contextual information as possible.

```python

splitter = RecursiveCharacterTextSplitter(

    chunk_size=500,

    chunk_overlap=100

)

```

#### Chunk Size

A chunk size of **500 characters** was chosen to provide sufficient context without creating excessively large embeddings. Smaller chunks improve retrieval precision, while larger chunks preserve more context.

#### Chunk Overlap

An overlap of **100 characters** ensures that important information spanning chunk boundaries is not lost during retrieval.

```text

Chunk 1

-------------------------

.................ABCDE


Chunk 2

               ABCDE..............

```

Without overlap, related information split between two chunks could become difficult to retrieve accurately.

#### Chunk Generation

Each interview document is read, split into chunks, and converted into LangChain `Document` objects before being stored in the vector database.

```python

chunks = splitter.split_text(text)


documents.append(

    Document(

        page_content=chunk,

        metadata={

            "source": file.name

        }

    )

)

```

The generated chunks are then passed to the embedding pipeline, forming the input for the vector database.

---

### 04. Vector Database

#### Overview

Once the documents have been chunked and converted into embeddings, they are stored inside a vector database. VIVA uses **ChromaDB** as its vector store to efficiently manage embeddings and perform semantic retrieval during the interview.

Unlike traditional databases that store structured records, a vector database stores numerical vector representations along with their associated metadata.

#### Creating the Vector Database

After all document chunks have been processed, they are stored in ChromaDB.

```python

db = Chroma.from_documents(

    documents=documents,

    embedding=embeddings,

    persist_directory="data/vector_store"

)

```

Each chunk is embedded using `nomic-embed-text` before being indexed inside the database.

This allows VIVA to trace retrieved information back to the original knowledge base document during debugging and evaluation.

---

### 05. Retrieval

#### Overview

The retrieval stage is responsible for finding the most relevant information from the vector database for a given interview question. Instead of searching documents using keywords, VIVA performs **semantic retrieval**, allowing it to identify contextually similar content even when different wording is used.

#### Creating the Retriever

VIVA converts the ChromaDB instance into a retriever that performs similarity search.

```python

retriever = db.as_retriever(

    search_kwargs={

        "k": 3

    }

)

```

The `k` parameter specifies the number of most relevant document chunks to retrieve for each query.

#### Similarity Search

The retrieval process is based on **semantic similarity**, not exact keyword matching. Documents with meanings similar to the query are ranked higher, enabling VIVA to retrieve relevant technical knowledge even when different terminology is used.

---

### 06. Context Injection

#### Overview

Context Injection is the final stage of the RAG pipeline. After the retriever identifies the most relevant document chunks, this contextual information is injected into the evaluation prompt before it is sent to the LLM.

This transforms a standard LLM into a **Retrieval-Augmented Generation (RAG)** system by allowing it to reason using external knowledge instead of relying solely on its pre-trained parameters.

#### Retrieving Context

Before evaluating a candidate's answer, VIVA retrieves the most relevant knowledge base documents.

```python

retrieved_docs = retrieve(question)

```

The retrieved chunks contain the technical information required to evaluate the candidate's response accurately.

#### Injecting Context

The retrieved context is passed to the evaluation chain along with the interview question and the candidate's answer.

```python

feedback = evaluation_chain.invoke(

    {

        "context": retrieved_docs,

        "question": question,

        "answer": answer

    }

)

```

The language model now evaluates the response using both the retrieved knowledge and the candidate's answer.

**Without context injection, the LLM would rely entirely on its internal knowledge, increasing the likelihood of hallucinations and inconsistent evaluations.**

---

## Interview Engine

### Overview

The Interview Engine is responsible for managing the complete interview lifecycle. It coordinates question generation, candidate responses, answer evaluation, adaptive difficulty, session management, and report generation to create a structured interview experience.

### Session Management

Each interview session maintains the complete history of questions, answers, and evaluation results.

```python

session.add_result(

    question,

    answer,

    feedback

)

```

This history is later used to generate the final interview report.

### Difficulty Management

VIVA dynamically adjusts interview difficulty based on the candidate's performance.

```python

difficulty = difficulty_manager.get_next_difficulty(

    score

)

```

This allows the interview to gradually become more challenging for stronger candidates while remaining accessible for beginners.

### Report Generation

After the interview concludes, all session data is compiled into a structured report.

```python

report = generate_report(

    session.get_history()

)

```

---

## Voice Pipeline

### Overview

The Voice Pipeline enables VIVA to conduct interviews through natural spoken conversations. It converts the interview process from a traditional text-based interaction into a fully voice-driven experience by integrating Speech-to-Text (STT) and Text-to-Speech (TTS).

This allows candidates to communicate naturally while the system listens, understands, evaluates, and responds entirely through voice.

### Speech-to-Text

VIVA uses **Faster-Whisper** to convert spoken responses into text.

```python

audio_file = record_audio(duration=15)


answer = transcribe(audio_file)

```

The transcribed text becomes the input for the RAG evaluation pipeline, allowing the interview engine to process spoken responses in the same way as typed input.

### Text-to-Speech

Interview questions and evaluation summaries are converted into speech using a local Text-to-Speech engine.

```python

text_to_speech(question)


text_to_speech(spoken_feedback)

```

This enables VIVA to interact with candidates naturally without requiring them to read terminal output.

Each iteration of the loop completes a full conversational cycle before proceeding to the next interview question.

---
