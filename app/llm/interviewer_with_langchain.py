from app.langchain.chains import (
    question_chain
)

def generate_question():

    result = question_chain.invoke(
        {
            "topic": "Vector Database"
        }
    )

    return result.content