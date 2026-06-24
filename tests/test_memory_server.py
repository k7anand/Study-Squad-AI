from mcp_servers.memory_server import save_quiz_result, get_quiz_history, get_weak_topics



def main():
    
    save_quiz_result("Math", "Fractions", 60)
    save_quiz_result("Science", "Forces", 85)

    print("\nQuiz History")
    print(get_quiz_history())

    print("\nWeak Topics")
    print(get_weak_topics())



if __name__ == "__main__":
    main()
