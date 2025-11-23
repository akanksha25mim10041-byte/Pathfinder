def calculate_scores(responses):
    scores = {
        "STEM": 0,
        "ARTS": 0,
        "SOCIAL": 0,
        "BUSINESS": 0,
        "TECH": 0
    }

    for domain, value in responses:
        scores[domain] += value

    return scores
