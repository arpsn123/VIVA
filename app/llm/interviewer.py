from ollama import chat


def generate_question():

    response = chat(
        model="gemma4:e2b",
        messages=[
            {
                "role": "system",
                "content": open(
                    "app\prompts\interviewer_prompt.txt",
                    encoding="utf-8"
                ).read()
            },
            {
                "role": "user",
                "content": "Ask me one interview question."
            }
        ]
    )

    return response.message.content
