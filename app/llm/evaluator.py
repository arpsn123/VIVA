from ollama import chat
import json


def evaluate_answer(question, answer):
    prompt = open("app\prompts\evaluator_prompt.txt", encoding="utf-8").read()
    response = chat(
        model="gemma4:e2b",

        messages=[
            {"role": "system", "content": prompt},
            {
                "role": "user",
                "content": f"""Question:{question}
                               Candidate Answer:{answer}
                            """,
            },
        ],
    )
    response_text = response.message.content
    
    try: # try-cath because the LLM sometimes misbehaves;
        # converting the response into JSON;
        result = json.loads(response_text)
    except:
        result = {
            "score": 0,
            "strengths": ["Parsing failed"],
            "weaknesses": ["Invalid JSON"],
            "improvement": "Retry"}

    return result
    # return response.message.content
