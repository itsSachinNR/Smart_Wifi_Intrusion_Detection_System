def generate_alert(score):
    if score >= 60:
        return "HIGH RISK"
    elif score >= 30:
        return "MEDIUM RISK"
    else:
        return "LOW RISK"
