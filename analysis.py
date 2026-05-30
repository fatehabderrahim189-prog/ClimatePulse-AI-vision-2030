def analyze_prediction(score):
    if score >= 75:
        return {
            "risk": "LOW",
            "message": "Climate conditions are stable"
        }

    elif score >= 50:
        return {
            "risk": "MEDIUM",
            "message": "Moderate climate impact detected"
        }

    else:
        return {
            "risk": "HIGH",
            "message": "Severe climate impact warning"
        }