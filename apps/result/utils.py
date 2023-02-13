def score_grade(score):
    if score > 100:
        return ValueError
    elif score >= 70:
        return "A"
    elif score >= 60 < 70:
        return "B"
    elif score >= 50 < 60:
        return "C"
    elif score >= 40 < 50:
        return "D"
    elif score >= 0 < 40:
        return "F"
    elif score < 0:
        return ValueError

