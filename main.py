from app.llm.interviewer_with_langchain import generate_question
from app.llm.evaluator_with_langchain import evaluate_answer
from app.interview.difficulty import DifficultyManager

# adding this so that the VIVA REMEMBERS WHAT EVER WE TALKED EARLIER;
from app.interview.session import InterviewSession
from app.interview.report import generate_report
import random

TOPICS = ["LLM", "Prompt Engineering", "Embeddings", "Vector Database", "RAG", "Token"]

session = InterviewSession()
difficulty_manager = DifficultyManager()

TOTAL_QUESTIONS = 3

difficulty = "medium"
# topic = "Embeddings"

for i in range(TOTAL_QUESTIONS):
    topic = random.choice(TOPICS)
    question = generate_question(topic, difficulty)

    print("QUESTION:")
    print(question)

    answer = input("\nYOUR ANSWER:\n")

    feedback = evaluate_answer(question, answer)

    # after evaluation, i am adding the question + answer + feedback to the session so that the machine can remember;
    session.add_result(question, answer, feedback)

    # taking score for the difficulty
    score = feedback["score"]
    difficulty = difficulty_manager.get_next_difficulty(score)

 
report = generate_report(session.get_history())

print(f"\nFinal Report saved in : ", report)

