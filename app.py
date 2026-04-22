from flask import Flask, render_template
from core.detector import process_events

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze")
def analyze():
    results = process_events("data/events.json")

    final_results = []

    for item in results:
        final_results.append({
            "device_mac": item["device_mac"],
            "score": item["score"],
            "risk": item["risk"],       
            "reasons": item["reasons"]  
        })

    return render_template("result.html", results=final_results)


if __name__ == "__main__":
    app.run(debug=True)
