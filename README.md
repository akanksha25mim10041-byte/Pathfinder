# Pathfinder: Career Interest Survey

# Overview

This is a simple Python console application designed to help users identify potential career domains that align with their interests. The program guides the user through a short questionnaire, calculates scores across different career domains (STEM, Arts, Social, Business, Tech), and provides a suggested career path based on their highest-scoring domain.

# Features

User Introduction: Gathers the user's name and grade/class.
Interactive Questionnaire: Presents a set of interest-based statements for the user to rate on a scale of 1 to 5.
Domain Scoring: Calculates a score for five distinct career domains: STEM, ARTS, SOCIAL, BUSINESS, and TECH.
Personalized Recommendation: Identifies the user's strongest domain and suggests a list of relevant career paths within that area.
Modular Design: The project is organized into separate Python modules for clear structure and maintainability (main.py, module_intro.py, module_questions.py, module_scorer.py, module_recommender.py).

# Technologies/Tools Used

Python 3: The core programming language used for the application logic.

--> Steps to Install & Run the Project

Prerequisites
You need to have Python 3 installed on your system.

--> Installation

1.Clone the Repository (or download the files):
Bash
git clone [YOUR_REPOSITORY_URL]
cd [YOUR_REPOSITORY_DIRECTORY]

2.Ensure all project files are in the same directory:
main.py
module_intro.py
module_questions.py
module_scorer.py
module_recommender.py

--> Running the Application

1.Open your terminal or command prompt.

2.Navigate to the directory where you saved the files.

3.Execute the main script:

Bash

python main.py

Follow the on-screen prompts to enter your name, grade, and complete the survey.

# Instructions for Testing

To test the application's core logic, you can focus on how different response inputs affect the final scores and recommendations.

1. Test Input Handling
   
Verify that the question module correctly handles valid and invalid inputs:
Valid Input: Enter numbers between 1 and 5 (e.g., 3, 5, 1). The program should accept them.
Invalid Input (Range): Enter numbers outside the 1-5 range (e.g., 0, 6). The program should prompt you with "Please enter a number between 1 and 5."
Invalid Input (Type): Enter non-numeric characters (e.g., abc). The program should prompt you with "Invalid input. Please enter a number."

2. Test Scoring Logic
   
The scoring system simply sums up the rating (1-5) for each question that belongs to a specific domain.
To Test for a STEM Recommendation: When running the survey, give a high score (e.g., 5) to the STEM-related question:
"I enjoy solving mathematical or logical problems."
Give low scores (e.g., 1 or 2) to all other questions. The final result should identify STEM as your strongest domain.
To Test for an ARTS Recommendation: Give a high score (e.g., 5) to the ARTS-related question:
"I like creating art, music, or writing stories."
Give low scores to all other questions. The final result should identify ARTS as your strongest domain and suggest careers like "Graphic Designer" or "Musician"
