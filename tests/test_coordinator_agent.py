from agents.coordinator_agent import CoordinatorAgent



def main():

    coordinator = CoordinatorAgent()

    results = coordinator.complete_learning_session(
        subject = "Math", topic = "Fractions", score = 60
    )

    print("\nSession Results:\n")
    print(f"Subject: {results['subject']}")
    print(f"Topic: {results['topic']}")
    print(f"Score: {results['score']}%")

    print("\nCoach Feedback:\n")
    print(results["coach_feedback"])

    print("\nRecommended Resources:\n")
    print(results["recommended_resources"])



if __name__ == "__main__":
    main()
