# Day 6: final report generation module

def generate_report(alerts, summary):
    with open("report.txt", "w") as file:
        file.write("SMART WIFI IDS - FINAL REPORT\n")
        file.write("Generated for Security Analysis\n")
        file.write("================================\n\n")

        # Alerts Section
        file.write("ALERTS:\n")
        file.write("--------\n")

        for alert in alerts:
            file.write(f"Device MAC: {alert['device_mac']}\n")
            file.write(f"Risk Level: {alert['risk']}\n")
            file.write("Reasons:\n")

            for reason in alert["reasons"]:
                file.write(f"- {reason}\n")

            file.write("\n")

        # Summary Section
        file.write("SUMMARY:\n")
        file.write("--------\n")

        for key, value in summary.items():
            file.write(f"{key}: {value}\n")
