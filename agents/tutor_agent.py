from skills.quiz_generation import generate_quiz



class TutorAgent:

    def generate_assessment(self, subject: str, topic: str, difficulty: str, num_questions: int = 3):

        print("Tutor Agent Activated!")
        print("Generating quiz...")

        return generate_quiz(subject = subject, topic = topic, difficulty = difficulty, num_questions = num_questions)
