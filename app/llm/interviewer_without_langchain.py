from ollama import chat


def generate_question():
    prompt = open("app\prompts\interviewer_prompt.txt",
                  encoding="utf-8").read()
    response = chat(  # this si the actual LLM call;
        model="gemma4:e2b",

        messages=[
            {
                "role": "system",  # this is the "SYSTEM MESSAGE", with this the LLM will behave like a INTERVIEWER as per the "interviewer_prompt.txt";
                "content": prompt},
            {
                "role": "user",  # this is the "USER MESSAGE", ask the question;
                "content": "Ask me one interview question."
            }
        ]
    )

    return response.message.content
