from module_intro import show_intro
from module_questions import ask_questions
from module_scorer import calculate_scores
from module_recommender import recommend_career

def main():
    name, grade = show_intro()
    responses = ask_questions()
    scores = calculate_scores(responses)
    recommend_career(scores, name)

main()
