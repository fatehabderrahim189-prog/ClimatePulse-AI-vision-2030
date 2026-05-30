def generate_policy(risk_level):
    if risk_level == "LOW":
        return "No action required. Conditions are stable."

    elif risk_level == "MEDIUM":
        return "Monitor conditions and reduce outdoor activity."

    else:
        return "Emergency alert: take preventive climate measures immediately."