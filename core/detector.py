
import json

def calculate_risk(event):
    score = 0

    if event["failed_attempts"] >= 5:
        score += 40

    if event["signal_strength"] < -80:
        score += 20

    if event["event_type"] == "auth_fail":
        score += 20
        
    if event.get("event_type") == "suspicious_login":
        score += 30

    if event.get("event_type") == "new_device":
        score += 20

    if event.get("location") == "unknown":
        score += 15

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
            "score": score,
            "event_type": event["event_type"]
        })

    return results
