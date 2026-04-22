from core.detector import process_events

results = process_events("data/events.json")

for r in results:
    print(f"[{r['risk']}] Device: {r['device_mac']} | Score: {r['score']}")
