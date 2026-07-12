# from app.llm.interviewer_with_langchain import generate_question
# from app.llm.evaluator_with_langchain import evaluate_answer
# from app.interview.difficulty import DifficultyManager

# # adding this so that the VIVA REMEMBERS WHAT EVER WE TALKED EARLIER;
# from app.interview.session import InterviewSession
# from app.interview.report import generate_report
# import random
# from app.voice.tts import text_to_speech
# from app.voice.player import play_audio
# from app.voice.stt import transcribe
# from app.voice.stt import record_audio

# TOPICS = ["LLM", "Prompt Engineering", "Embeddings", "Vector Database", "RAG", "Token"]

# session = InterviewSession()
# difficulty_manager = DifficultyManager()

# TOTAL_QUESTIONS = 3

# difficulty = "easy"
# # topic = "Embeddings"

# for i in range(TOTAL_QUESTIONS):
#     topic = random.choice(TOPICS)
    
#     print("1. Generating Question")
#     question = generate_question(topic, difficulty)

#     print("\nQUESTION:")
#     print(question)

#     # for the edge_tts(microsoft)
#     # asyncio.run(text_to_speech(question))
#     # play_audio("response.mp3")

#     print("2. Speaking Question")
#     # for the pyttsx3(local runs on gpu)
#     text_to_speech(question)

#     # answer = input("\nYOUR ANSWER:\n")

#     print("3. Listening...")
#     audio_file = record_audio(duration=15)
    
#     print("4. Transcribing")
#     answer = transcribe(audio_file)
#     print("\nYOU SAID:")
#     print(answer)

#     print("5. Evaluating")
#     feedback = evaluate_answer(question, answer)

#     # after evaluation, i am adding the question + answer + feedback to the session so that the machine can remember;
#     session.add_result(question, answer, feedback)

#     # taking score for the difficulty
#     score = feedback["score"]
#     difficulty = difficulty_manager.get_next_difficulty(score)

#     improvement = feedback["improvement"]
#     spoken_feedback = f"""
#     Your score is {score} out of 10.
#     {improvement}
#     """
#     # asyncio.run(text_to_speech(spoken_feedback))
#     # play_audio("response.mp3")
#     print("6. Speaking Feedback")
#     text_to_speech(spoken_feedback)
#     print("7. End Of Loop")


# report = generate_report(session.get_history())

# print(f"\nFinal Report saved in : ", report)


from app.llm.interviewer_with_langchain import generate_question
from app.llm.evaluator_with_langchain import evaluate_answer
from app.interview.difficulty import DifficultyManager
from app.interview.session import InterviewSession
from app.interview.report import generate_report

from app.voice.tts import text_to_speech
from app.voice.stt import transcribe, record_audio

import random
import time

from rich.console import Console
from rich.panel import Panel
from rich.rule import Rule
from rich.table import Table

console = Console()



TOPICS = [
    "LLM",
    "Prompt Engineering",
    "Embeddings",
    "Vector Database",
    "RAG",
    "Token"
]

TOTAL_QUESTIONS = 3

session = InterviewSession()
difficulty_manager = DifficultyManager()

difficulty = "easy"

console.print()

console.print(
    Panel.fit(
        "[bold cyan]🎙️ VIVA[/bold cyan]\n"
        "[white]Voice Interview & Verification Assistant[/white]",
        border_style="bright_blue"
    )
)

console.print()


modules = [
    "Loading Gemma...",
    "Loading LangChain...",
    "Loading ChromaDB...",
    "Loading Whisper...",
    "Loading Voice Pipeline...",
    "Initializing Interview Engine..."
]

for module in modules:

    with console.status(
        f"[cyan]{module}[/cyan]"
    ):

        time.sleep(0.7)

    console.print(
        f"[green]✓[/green] {module.replace('Loading ','').replace('Initializing ','').replace('...','')} Ready"
    )

console.print()

console.rule("[bold green]Interview Started[/bold green]")


for i in range(TOTAL_QUESTIONS):

    topic = random.choice(TOPICS)

    console.print(
        Rule(
            f"[bold yellow]Question {i+1}/{TOTAL_QUESTIONS}[/bold yellow]"
        )
    )

    question = generate_question(
        topic,
        difficulty
    )

    console.print()

    console.print(
        Panel(
            question,
            title="[bold cyan]Interview Question[/bold cyan]",
            border_style="cyan"
        )
    )

    text_to_speech(question)

    console.print()

    console.print(
        "[bold yellow]🎤 Listening...[/bold yellow]"
    )

    audio_file = record_audio(
        duration=15
    )

    console.print(
        "[bold blue]📝 Transcribing...[/bold blue]"
    )

    answer = transcribe(audio_file)

    console.print()

    console.print(
        Panel(
            answer,
            title="[bold green]Candidate Response[/bold green]",
            border_style="green"
        )
    )

    console.print(
        "[bold magenta]🧠 Evaluating Answer...[/bold magenta]"
    )

    feedback = evaluate_answer(
        question,
        answer
    )

    session.add_result(
        question,
        answer,
        feedback
    )

    score = feedback["score"]

    difficulty = difficulty_manager.get_next_difficulty(
        score
    )

    improvement = feedback["improvement"]


    table = Table(
        title="Evaluation Report"
    )

    table.add_column(
        "Metric",
        style="cyan",
        justify="left"
    )

    table.add_column(
        "Result",
        style="green"
    )

    table.add_row(
        "Score",
        f"{score}/10"
    )

    table.add_row(
        "Improvement",
        improvement
    )

    console.print()

    console.print(table)

    spoken_feedback = f"""
    Your score is {score} out of 10.
    {improvement}
    """

    text_to_speech(
        spoken_feedback
    )

console.rule("[bold green]Interview Completed[/bold green]")

report = generate_report(
    session.get_history()
)

console.print()

console.print(
    Panel.fit(
        f"[bold green]✓ Interview Report Generated[/bold green]\n\n{report}",
        title="Report",
        border_style="green"
    )
)