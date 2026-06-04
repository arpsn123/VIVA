from ollama import chat


def evaluate_answer(question, answer):
    prompt = open("app\prompts\evaluator_prompt.txt", encoding="utf-8").read()
    response = chat(
        model="gemma4:e2b",
        messages=[
            {"role": "system", "content": prompt},
            {
                "role": "user",
                "content": f"""
Question:
{question}

Candidate Answer:
{answer}
""",
            },
        ],
    )

    return response.message.content
