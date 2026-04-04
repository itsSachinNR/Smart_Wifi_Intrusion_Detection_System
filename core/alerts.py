# Final version: Alerts module ready for integration and demo

# Day 1: Initial alerts module setup
from reports.report_generator import generate_report


# Day 2: Convert score into risk level
def generate_alert(score):
    if score >= 60:
        return "HIGH RISK"
    elif score >= 30:
        return "MEDIUM RISK"
    else:
        return "LOW RISK"


# Day 3: Format alert data
def format_alert(device_mac, score, reasons):
    risk = generate_alert(score)
    return {
        "device_mac": device_mac,
        "risk": risk,
        "reasons": reasons
    }


# Day 4: Build full alert from detector output
def build_full_alert(event_result):
    return format_alert(
        event_result["device_mac"],
        event_result["score"],
        event_result["reasons"]
    )


# Day 4: Update summary counts
def update_summary(summary, alert):
    risk = alert["risk"]
    if risk in summary:
        summary[risk] += 1
    else:
        summary[risk] = 1


# Day 3: Print alert nicely
def print_alert(alert):
    print("========== ALERT ==========")
    print(f"Device MAC : {alert['device_mac']}")
    print(f"Risk Level : {alert['risk']}")
    print("Reasons:")
    for reason in alert["reasons"]:
        print(f" - {reason}")
    print("===========================\n")


# Day 7: Validate alert structure
def validate_alert(alert):
    return all([
        "device_mac" in alert,
        "risk" in alert,
        "reasons" in alert
    ])


# MAIN EXECUTION
if __name__ == "__main__":
    summary = {}
    alerts_list = []

    sample_data = [
        {"device_mac": "AA", "score": 75, "reasons": ["failed attempts"]},
        {"device_mac": "BB", "score": 40, "reasons": ["weak signal"]},
        {"device_mac": "CC", "score": 10, "reasons": ["normal"]},
        {"device_mac": "DD", "score": 80, "reasons": ["unknown device"]},
    ]

    for event in sample_data:
        alert = build_full_alert(event)

        if validate_alert(alert):
            alerts_list.append(alert)
            update_summary(summary, alert)
            print_alert(alert)

    # Day 7: final clean summary display
    print("\n===== FINAL SUMMARY =====")
    for key, value in summary.items():
        print(f"{key}: {value}")
    print("=========================\n")

    # Generate report
    generate_report(alerts_list, summary)
