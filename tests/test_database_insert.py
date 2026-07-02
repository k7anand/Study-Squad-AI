from database import initialize_database, insert_quiz_result, get_all_quiz_results, clear_database



def main():
    initialize_database()
    insert_quiz_result("Math", "Fractions", 80)
    insert_quiz_result("Science", "Forces", 65)
    print(get_all_quiz_results())
    clear_database()
    print(get_all_quiz_results())
    insert_quiz_result("Science", "Forces", 65)
    print(get_all_quiz_results())



if __name__ == "__main__":
    main()
