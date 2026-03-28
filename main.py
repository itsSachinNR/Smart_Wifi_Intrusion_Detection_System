from core.detector import process_events
from core.alerts import generate_alert

results = process_events("data/events.json")

for r in results:
    risk = generate_alert(r["score"])
    print(f"Device: {r['device_mac']} | Score: {r['score']} | Risk: {risk}")
