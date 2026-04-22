import json

def calculate_risk(event):
    score = 0

    # failed attempts
    if event.get("failed_attempts", 0) >= 7:
        score += 50
    elif event.get("failed_attempts", 0) >= 4:
        score += 30

    # signal strength
    if event.get("signal_strength", 0) < -85:
        score += 25
    elif event.get("signal_strength", 0) < -75:
        score += 15

    # event types
    if event.get("event_type") == "auth_fail":
        score += 25
    elif event.get("event_type") == "suspicious_login":
        score += 30
    elif event.get("event_type") == "new_device":
        score += 20

    # optional fields
    if event.get("location") == "unknown":
        score += 20

    if event.get("is_known_device") == False:
        score += 25

    return score


def get_risk_level(score):
    if score >= 80:
        return "HIGH RISK"
    elif score >= 40:
        return "MEDIUM RISK"
    else:
        return "LOW RISK"


def process_events(file_path):
    with open(file_path, "r") as f:
        events = json.load(f)

    results = []

    for event in events:
        score = calculate_risk(event)
        risk = get_risk_level(score)

        results.append({
            "device_mac": event.get("device_mac"),
            "score": score,
            "risk": risk,
            "event_type": event.get("event_type")
        })

    return results
