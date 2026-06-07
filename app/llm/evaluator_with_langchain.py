import json

from app.langchain.chains import (
    evaluation_chain

)

def evaluate_answer(question, answer):

    result = evaluation_chain.invoke(
        {
            "question": question,
            "answer": answer
        })

    response = result.content

    try:
        parsed = json.loads(response)
        return parsed

    except:
        return {
            "score": 0,
            "strengths": [
                "Failed to parse model output"
            ],
            "weaknesses": [
                "Invalid JSON returned"
            ],
            "improvement":
            "Check evaluator prompt"
        }
