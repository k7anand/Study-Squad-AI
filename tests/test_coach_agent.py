from mcp_servers.memory_server import save_quiz_result
from agents.coach_agent import CoachAgent



def main():

    save_quiz_result("Math", "Fractions", 60)
    save_quiz_result("Science", "Forces", 85)

    coach = CoachAgent()

    print("\nRule-Based Coach:")
    print(coach.analyze_progress())

    print("\nAI Coach:")
    print(coach.analyze_progress_ai())



if __name__ == "__main__":
    main()
