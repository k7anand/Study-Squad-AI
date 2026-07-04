from agents.resource_agent import ResourceAgent



def main():

    agent = ResourceAgent()

    print("\nRule-Based Resource Agent:\n")
    print(agent.recommend_resources("Fractions"))

    print("\nAI Resource Agent:\n")
    print(agent.recommend_resources_ai(topic = "Fractions", difficulty = "Beginner"))



if __name__ == "__main__":
    main()

