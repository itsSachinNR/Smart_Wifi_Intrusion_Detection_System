import json


def calculate_risk(event):
    score = 0
    reasons = []

    # failed attempts
    if event.get("failed_attempts", 0) >= 7:
        score += 50
        reasons.append("High failed attempts")

    elif event.get("failed_attempts", 0) >= 4:
        score += 30
        reasons.append("Moderate failed attempts")

    # signal strength
    if event.get("signal_strength", 0) < -85:
        score += 25
        reasons.append("Very weak signal")

    elif event.get("signal_strength", 0) < -75:
        score += 15
        reasons.append("Weak signal")

    # event types
    if event.get("event_type") == "auth_fail":
        score += 25
        reasons.append("Authentication failure")

    elif event.get("event_type") == "suspicious_login":
        score += 30
        reasons.append("Suspicious login attempt")

    elif event.get("event_type") == "new_device":
        score += 20
        reasons.append("New unknown device detected")

    # optional fields
    if event.get("location") == "unknown":
        score += 20
        reasons.append("Unknown location")

    if event.get("is_known_device") is False:
        score += 25
        reasons.append("Unrecognized device")

    return score, reasons


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
        score, reasons = calculate_risk(event)
        risk = get_risk_level(score)

        results.append({
            "device_mac": event.get("device_mac"),
            "score": score,
            "risk": risk,
            "event_type": event.get("event_type"),
            "reasons": reasons   # ✅ IMPORTANT (for alerts + report)
        })

    return results
