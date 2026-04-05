from flask import Flask, render_template
from core.detector import process_events
from core.alerts import generate_alert

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze")
def analyze():
    results = process_events("data/events.json")

    final_results = []

    for item in results:
        risk = generate_alert(item["score"])

        final_results.append({
            "device_mac": item["device_mac"],
            "score": item["score"],
            "risk": risk,
            "reason": item["event_type"]
        })

    return render_template("result.html", results=final_results)

if __name__ == "__main__":
    app.run(debug=True)