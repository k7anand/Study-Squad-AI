from adk_app.quiz_tool import quiz_generation_tool



def main():

    quiz = quiz_generation_tool(subject = "Math", topic = "Fractions", difficulty = "Beginner", num_questions = 3)


    for i, question in enumerate(quiz, start = 1):

        print(f"\nQuestion {i}")
        print(question["question"])

        for key, value in question["options"].items():
            print(f"{key}. {value}")

        print(f"Correct Answer: {question['answer']}")



if __name__ == "__main__":
    main()
