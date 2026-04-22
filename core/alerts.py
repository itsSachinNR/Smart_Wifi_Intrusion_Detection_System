# Final version: Alerts module ready for integration and demo

from reports.report_generator import generate_report


# Convert score into risk level (used if needed separately)
def generate_alert(score):
    if score >= 60:
        return "HIGH RISK"
    elif score >= 30:
        return "MEDIUM RISK"
    else:
        return "LOW RISK"


# Format alert data
def format_alert(device_mac, score, reasons):
    risk = generate_alert(score)
    return {
        "device_mac": device_mac,
        "risk": risk,
        "reasons": reasons
    }


# Build full alert from detector output
def build_full_alert(event_result):
    return {
        "device_mac": event_result.get("device_mac"),
        "risk": event_result.get("risk"),   # use detector's risk directly ✅
        "reasons": event_result.get("reasons", [])
    }


# Update summary counts
def update_summary(summary, alert):
    risk = alert["risk"]
    summary[risk] = summary.get(risk, 0) + 1


# Print alert nicely (for CLI)
def print_alert(alert):
    print("========== ALERT ==========")
    print(f"Device MAC : {alert['device_mac']}")
    print(f"Risk Level : {alert['risk']}")
    print("Reasons:")

    for reason in alert["reasons"]:
        print(f" - {reason}")

    print("===========================\n")


# Validate alert structure
def validate_alert(alert):
    return all([
        "device_mac" in alert,
        "risk" in alert,
        "reasons" in alert
    ])


# Optional: Full pipeline runner (for testing/demo)
def run_alert_pipeline(results):
    summary = {}
    alerts_list = []

    for event in results:
        alert = build_full_alert(event)

        if validate_alert(alert):
            alerts_list.append(alert)
            update_summary(summary, alert)
            print_alert(alert)

    # Print summary
    print("\n===== FINAL SUMMARY =====")
    for key, value in summary.items():
        print(f"{key}: {value}")
    print("=========================\n")

    # Generate report file
    generate_report(alerts_list, summary)


# MAIN EXECUTION (for standalone testing)
if __name__ == "__main__":
    sample_data = [
        {"device_mac": "AA", "score": 75, "risk": "HIGH RISK", "reasons": ["High failed attempts"]},
        {"device_mac": "BB", "score": 40, "risk": "MEDIUM RISK", "reasons": ["Weak signal"]},
        {"device_mac": "CC", "score": 10, "risk": "LOW RISK", "reasons": ["Normal activity"]},
        {"device_mac": "DD", "score": 80, "risk": "HIGH RISK", "reasons": ["Unknown device"]},
    ]

    run_alert_pipeline(sample_data)
