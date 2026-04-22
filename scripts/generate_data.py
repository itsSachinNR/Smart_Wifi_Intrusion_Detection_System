import json
import random
from datetime import datetime, timedelta

events = []

for i in range(15):
    event = {
        "timestamp": str(datetime.now() + timedelta(minutes=i)),
        "device_mac": f"AA:BB:CC:{random.randint(10,99)}:{random.randint(10,99)}:{random.randint(10,99)}",
        "ssid": "HomeWiFi",
        "event_type": random.choice(["normal", "auth_fail"]),
        "failed_attempts": random.randint(0, 10),
        "signal_strength": random.randint(-90, -50)
    }
    events.append(event)

with open("data/events.json", "w") as f:
    json.dump(events, f, indent=2)

print("Sample data generated!")
