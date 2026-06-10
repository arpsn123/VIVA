from app.langchain.chains import (
    question_chain
)

def generate_question(topic, difficulty):

    result = question_chain.invoke(
        {
            "topic": topic,
            "difficulty": difficulty
        }
    )

    return result.content