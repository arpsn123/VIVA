import json
from app.rag.retriever import retrieve
from app.langchain.chains import evaluation_chain


def evaluate_answer(question, answer):

    retrieved_docs = retrieve(question)

    context = "\n\n".join([doc.page_content for doc in retrieved_docs])
    
    result = evaluation_chain.invoke(
        {"context": context, "question": question, "answer": answer}
    )

    response = result.content

    try:
        parsed = json.loads(response)
        return parsed

    except:
        return {
            "score": 0,
            "strengths": ["Failed to parse model output"],
            "weaknesses": ["Invalid JSON returned"],
            "improvement": "Check evaluator prompt",
        }
