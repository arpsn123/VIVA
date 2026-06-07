from app.llm.interviewer_with_langchain import generate_question
from app.llm.evaluator_with_langchain import evaluate_answer

print("\n===== VIVA =====\n")

question = generate_question()

print("QUESTION:")
print(question)

answer = input("\nYOUR ANSWER:\n")

feedback = evaluate_answer(question, answer)

print("\nFEEDBACK:\n")
# print(feedback) # this would be good for the text style response, but as i am returing a JSON in feedback i need a upgradation;
print("\nSCORE:")
print(feedback["score"])

print("\nSTRENGTHS:")
for item in feedback["strengths"]:
    print("-", item)

print("\nWEAKNESSES:")
for item in feedback["weaknesses"]:
    print("-", item)

print("\nIMPROVEMENT:")
print(feedback["improvement"])
