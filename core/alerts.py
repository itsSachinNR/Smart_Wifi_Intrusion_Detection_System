# Day 1: Initial alerts module setup
from reports.report_generator import generate_report
def generate_alert(score):
    if score >= 60:
        return "HIGH RISK"
    elif score >= 30:
        return "MEDIUM RISK"
    else:
        return "LOW RISK"


def format_alert(device_mac, score, reasons):
    risk = generate_alert(score)

    return {
        "device_mac": device_mac,
        "risk": risk,
        "reasons": reasons
    }


def build_full_alert(event_result):
    return format_alert(
        event_result["device_mac"],
        event_result["score"],
        event_result["reasons"]
    )


def update_summary(summary, alert):
    risk = alert["risk"]

    if risk in summary:
        summary[risk] += 1
    else:
        summary[risk] = 1

 


# Day 5: generate final report output
def generate_report(alerts, summary):
    with open("report.txt", "w") as file:
        file.write("SMART WIFI IDS REPORT\n")
        file.write("======================\n\n")

        file.write("ALERTS:\n")
        file.write("--------\n")

        for alert in alerts:
            file.write(f"Device MAC: {alert['device_mac']}\n")
            file.write(f"Risk Level: {alert['risk']}\n")
            file.write("Reasons:\n")

            for reason in alert["reasons"]:
                file.write(f"- {reason}\n")

            file.write("\n")

        file.write("SUMMARY:\n")
        file.write("--------\n")

        for key, value in summary.items():
            file.write(f"{key}: {value}\n")

# Day 7: ensure alert structure is valid
def validate_alert(alert):
    return all([
        "device_mac" in alert,
        "risk" in alert,
        "reasons" in alert
    ])

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

    generate_report(alerts_list, summary)
