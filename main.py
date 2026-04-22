from core.detector import process_events

# Run detection
results = process_events("data/events.json")

# Header
print("\n==========================================")
print("   Smart WiFi Intrusion Detection Report  ")
print("==========================================\n")

# Display each result
for r in results:
    print(f"[{r['risk']}] Device: {r['device_mac']} | Score: {r['score']}")

# Footer
print("\n==========================================")
print("               End of Report              ")
print("==========================================\n")

# Summary calculation
high = sum(1 for r in results if r["risk"] == "HIGH RISK")
medium = sum(1 for r in results if r["risk"] == "MEDIUM RISK")
low = sum(1 for r in results if r["risk"] == "LOW RISK")

# Summary output
print("Summary:")
print(f"🔴 HIGH RISK   : {high}")
print(f"🟠 MEDIUM RISK : {medium}")
print(f"🟢 LOW RISK    : {low}")
