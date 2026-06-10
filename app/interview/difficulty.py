class DifficultyManager:

    def get_next_difficulty(self, score):

        if score >= 8:
            return "hard"

        elif score >= 5:
            return "medium"

        else:
            return "easy"