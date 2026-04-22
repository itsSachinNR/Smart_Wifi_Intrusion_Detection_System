from core.detector import process_events

results = process_events("data/events.json")

print("\n=== Smart WiFi Intrusion Detection Report ===\n")

for r in results:
    print(f"[{r['risk']}] Device: {r['device_mac']} | Score: {r['score']}")

print("\n=== End of Report ===\n")
