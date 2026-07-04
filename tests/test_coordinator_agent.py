from agents.coordinator_agent import CoordinatorAgent



def main():

    coordinator = CoordinatorAgent()

    session = coordinator.run_learning_session(subject = "Math", topic = "Fractions", difficulty = "Beginner")
    quiz = session["quiz"]
    student_answers = ["A", "D", "B"]
    results = coordinator.complete_learning_session(subject = "Math", topic = "Fractions", difficulty = "Beginner", quiz = quiz, student_answers = student_answers)

    print("\nSession Results:\n")
    print(results["grading_results"]["score"])
    print(results["grading_results"]["correct"])
    print(results["grading_results"]["missed_questions"])

    print("\nCoach Feedback:\n")
    print(results["coach_feedback"])

    print("\nRecommended Resources:\n")
    print(results["recommended_resources"])



if __name__ == "__main__":
    main()
