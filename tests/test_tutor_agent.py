from agents.tutor_agent import TutorAgent



def main():

    tutor = TutorAgent()

    quiz = tutor.generate_assessment(subject = "Math", topic = "Fractions", difficulty = "beginner", num_questions = 3)


    for i, question in enumerate(quiz, start = 1):

        print(f"\n Question {i}")
        print(question["question"])

        for key, value in question["options"].items():
            print(f"{key}. {value}")

        print(f"Correct Answer: {question['answer']}")



if __name__ == "__main__":
    main()
