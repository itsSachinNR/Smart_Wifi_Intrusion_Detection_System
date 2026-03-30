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
