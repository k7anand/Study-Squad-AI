from grading import grade_quiz


def main():

    quiz = [
        {"question": "Q1", "answer": "A"},
        {"question": "Q2", "answer": "C"},
        {"question": "Q3", "answer": "B"},
    ]

    student_answers = ["A", "D", "B"]

    results = grade_quiz(quiz, student_answers)

    print("\nQuiz Results:\n")
    print(f"Correct: {results['correct']}")
    print(f"Total: {results['total']}")
    print(f"Score: {results['score']}%")

    print("\nMissed Questions:\n")

    for question in results["missed_questions"]:
        print(question)


if __name__ == "__main__":
    main()
