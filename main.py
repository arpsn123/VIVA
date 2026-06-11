from app.llm.interviewer_with_langchain import generate_question
from app.llm.evaluator_with_langchain import evaluate_answer
from app.interview.difficulty import DifficultyManager

# adding this so that the VIVA REMEMBERS WHAT EVER WE TALKED EARLIER;
from app.interview.session import InterviewSession
from app.interview.report import generate_report
import random
from app.voice.tts import text_to_speech
from app.voice.player import play_audio
from app.voice.stt import transcribe
from app.voice.stt import record_audio

TOPICS = ["LLM", "Prompt Engineering", "Embeddings", "Vector Database", "RAG", "Token"]

session = InterviewSession()
difficulty_manager = DifficultyManager()

TOTAL_QUESTIONS = 3

difficulty = "easy"
# topic = "Embeddings"

for i in range(TOTAL_QUESTIONS):
    topic = random.choice(TOPICS)
    
    print("1. Generating Question")
    question = generate_question(topic, difficulty)

    print("\nQUESTION:")
    print(question)

    # for the edge_tts(microsoft)
    # asyncio.run(text_to_speech(question))
    # play_audio("response.mp3")

    print("2. Speaking Question")
    # for the pyttsx3(local runs on gpu)
    text_to_speech(question)

    # answer = input("\nYOUR ANSWER:\n")

    print("3. Listening...")
    audio_file = record_audio(duration=15)
    
    print("4. Transcribing")
    answer = transcribe(audio_file)
    print("\nYOU SAID:")
    print(answer)

    print("5. Evaluating")
    feedback = evaluate_answer(question, answer)

    # after evaluation, i am adding the question + answer + feedback to the session so that the machine can remember;
    session.add_result(question, answer, feedback)

    # taking score for the difficulty
    score = feedback["score"]
    difficulty = difficulty_manager.get_next_difficulty(score)

    improvement = feedback["improvement"]
    spoken_feedback = f"""
    Your score is {score} out of 10.
    {improvement}
    """
    # asyncio.run(text_to_speech(spoken_feedback))
    # play_audio("response.mp3")
    print("6. Speaking Feedback")
    text_to_speech(spoken_feedback)
    print("7. End Of Loop")


report = generate_report(session.get_history())

print(f"\nFinal Report saved in : ", report)
