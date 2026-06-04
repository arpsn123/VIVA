from app.llm.interviewer import generate_question
from app.llm.evaluator import evaluate_answer

print("\n===== VIVA =====\n")

question = generate_question()

print("QUESTION:")
print(question)

answer = input("\nYOUR ANSWER:\n")

feedback = evaluate_answer(
    question,
    answer
)

print("\nFEEDBACK:\n")
print(feedback)
