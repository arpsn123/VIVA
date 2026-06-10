
from datetime import datetime


def generate_report(history):

    scores = [item["feedback"]["score"] for item in history]

    average_score = sum(scores) / len(scores) if scores else 0

    report_lines = []

    report_lines.append("VIVA INTERVIEW REPORT")
    report_lines.append("")

    report_lines.append(f"Average Score: {average_score:.2f}/10")

    report_lines.append(f"Total Questions: {len(history)}")

    report_lines.append("")
    report_lines.append("INTERVIEW DETAILS")
    report_lines.append("")

    for idx, item in enumerate(history, start=1):

        report_lines.append(f"Question {idx}")

        report_lines.append(f"Question: {item['question']}")

        report_lines.append(f"Answer: {item['answer']}")

        report_lines.append(f"Score: {item['feedback']['score']}/10")

        report_lines.append("")
        report_lines.append("Strengths:")

        for strength in item["feedback"]["strengths"]:

            report_lines.append(f"• {strength}")

        report_lines.append("")
        report_lines.append("Weaknesses:")

        for weakness in item["feedback"]["weaknesses"]:

            report_lines.append(f"• {weakness}")

        report_lines.append("")
        report_lines.append("Improvement Suggestion:")

        report_lines.append(item["feedback"]["improvement"])

        report_lines.append("")
        report_lines.append("----------------------------------------")
        report_lines.append("")

    report_text = "\n".join(report_lines)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    filename = f"data/interview_report_{timestamp}.txt"

    with open(filename, "w", encoding="utf-8") as file:

        file.write(report_text)

    return filename
