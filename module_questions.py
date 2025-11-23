def get_questions():
    return [
        ("I enjoy solving mathematical or logical problems.", "STEM"),
        ("I like creating art, music, or writing stories.", "ARTS"),
        ("I enjoy helping people with their problems.", "SOCIAL"),
        ("I am interested in leading or managing groups.", "BUSINESS"),
        ("I like doing hands-on tasks like fixing or building things.", "TECH"),
    ]

def ask_questions():
    print("Rate each statement from 1 (Strongly Disagree) to 5 (Strongly Agree).")
    responses = []

    for question, code in get_questions():
        while True:
            try:
                answer = int(input(f"{question}\nYour answer (1-5): "))
                if 1 <= answer <= 5:
                    responses.append((code, answer))
                    break
                else:
                    print("Please enter a number between 1 and 5.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    
    return responses
