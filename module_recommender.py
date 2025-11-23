def recommend_career(scores, name):
    highest = max(scores, key=scores.get)
    
    career_paths = {
        "STEM": ["Engineer", "Scientist", "Data Analyst", "Software Developer"],
        "ARTS": ["Graphic Designer", "Musician", "Writer", "Animator"],
        "SOCIAL": ["Psychologist", "Teacher", "Social Worker", "Counsellor"],
        "BUSINESS": ["Manager", "Entrepreneur", "Marketing Specialist"],
        "TECH": ["Technician", "Mechanic", "Electrician"]
    }

    print("\n========================================")
    print("               RESULTS")
    print("========================================")
    print(f"Career Report for: {name}")
    print("\nYour Domain Scores:")
    for domain in scores:
        print(f"{domain}: {scores[domain]}")

    print(f"\nYour strongest career domain is: **{highest}**")
    print("\nSuggested Careers:")
    for career in career_paths[highest]:
        print(" -", career)
