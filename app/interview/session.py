class InterviewSession:

    def __init__(self):

        self.history = []

    def add_result(
        self,
        question,
        answer,
        feedback
    ):

        self.history.append(
            {
                "question": question,
                "answer": answer,
                "feedback": feedback
            }
        )

    def get_history(self):

        return self.history