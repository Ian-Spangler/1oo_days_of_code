# Exercise Tracker (My work)
import requests
import datetime as dt

APP_ID = "My application id"
API_KEY = "My api key"

nutrition_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

nutrition_paramas = {
    "query": input("Tell me which exercises you did: "),
    "gender": "male",
    "weight_kg": 70,
    "height_cm": 173,
    "age": 21,
}

nutrition_endpoint = "https://trackapi.nutritionix.com/v2/naural/exercise"

nutrition_response = requests.post(url=nutrition_endpoint, json=nutrition_paramas, headers=nutrition_headers)
result = nutrition_response.json()

USERNAME = "Ian"
PROJECT_NAME = "My Project"
SHEET_NAME = "My Workouts"

SHEETY_TOKEN = "My sheety token"

today = dt.datetime.now()
date = today.strftime("%Y/%m/%d")
time = today.strftime("%X")

sheety_headers = {
    "Authorization": f"Bearer {SHEETY_TOKEN}"
}

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

sheety_endpoint = f"https://api.sheety.co/{USERNAME}/{PROJECT_NAME}/{SHEET_NAME}"

sheety_response = requests.post(url=sheety_endpoint, json=sheet_inputs, headers=sheety_headers)