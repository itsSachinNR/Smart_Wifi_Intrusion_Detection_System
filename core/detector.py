import json

def calculate_risk(event):
    score = 0

    # failed attempts
    if event["failed_attempts"] >= 7:
        score += 50
    elif event["failed_attempts"] >= 4:
        score += 30

    # signal strength
    if event["signal_strength"] < -85:
        score += 25
    elif event["signal_strength"] < -75:
        score += 15

    # event types
    if event["event_type"] == "auth_fail":
        score += 25
    elif event["event_type"] == "suspicious_login":
        score += 30
    elif event["event_type"] == "new_device":
        score += 20

    # location
    if event.get("location") == "unknown":
        score += 20

    # known device check
    if event.get("is_known_device") == False:
        score += 25

    return score


def process_events(file_path):
    with open(file_path, "r") as f:
        events = json.load(f)

    results = []

    for event in events:
        score = calculate_risk(event)

        results.append({
            "device_mac": event["device_mac"],
            "score": score
        })

    return results
