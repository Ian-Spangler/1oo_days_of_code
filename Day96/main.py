from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

PERFECT_TENSE_URL = "https://api.perfecttense.com/correct"
APP_KEY = os.getenv("APP_KEY")
USER_KEY = os.getenv("USER_API_KEY")

@app.route("/", methods=["GET", "POST"])
def index():
    original = ""
    corrected = ""
    score = None

    if request.method == "POST":
        original = request.form.get("text_input")

        headers = {
            "Authorization": USER_KEY,
            "AppAuthorization": APP_KEY,
            "Content-Type": "application/json"
        }

        data = {
            "text": original,
            "responseType": ["corrected", "grammarScore"]
        }

        response = requests.post(PERFECT_TENSE_URL, json=data, headers=headers)

        if response.status_code == 200:
            result = response.json()
            corrected = result.get("corrected", "")
            score = result.get("grammarScore")

    return render_template("index.html", original=original,
                           corrected=corrected, score=score)

if __name__ == "__main__":
    app.run(debug=True)
