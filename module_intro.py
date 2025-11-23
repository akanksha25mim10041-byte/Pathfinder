def show_intro():
    print("========================================")
    print("          CAREER INTEREST SURVEY")
    print("========================================")
    print("This survey will help you understand which career")
    print("domains match your interests.")
    print()

    name = input("Enter your name: ")
    grade = input("Enter your class/grade: ")
    
    print(f"\nWelcome {name} from Class {grade}!")
    print("Let's begin the survey...\n")

    return name, grade
