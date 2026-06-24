from skills.quiz_generation import generate_quiz


def quiz_generation_tool(subject: str, topic: str, difficulty: str, num_questions: int = 3):
    """
    Generate a multiple-choice quiz on a specified topic.
    """
    print("QUIZ TOOL CALLED!")
    return generate_quiz(subject = subject, topic = topic, difficulty = difficulty, num_questions = num_questions)
