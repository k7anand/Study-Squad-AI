from skills.quiz_generation import generate_quiz


def main():

    quiz = generate_quiz(subject = "Math", topic = "Fractions", difficulty = "Beginner", num_questions = 3)

    for i, question in enumerate(quiz, start = 1):

        print(f"Question {i}")
        print(question["question"])

        for key, value in question["options"].items():
            print(f"{key}. {value}")

        print(f"Correct answer: {question['answer']}")



if __name__ == "__main__":
    main()
