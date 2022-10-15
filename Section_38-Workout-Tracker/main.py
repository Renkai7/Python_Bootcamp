import os
import requests
from datetime import datetime

# CONSTANTS
APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
BEARER_TOKEN = os.environ.get("BEARER_TOKEN")

# Endpoints
nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/"
exercise_endpoint = f"{nutritionix_endpoint}natural/exercise"
sheety_endpoint = "https://api.sheety.co/8b4b6d38f07f44ff2c34f43d12529f0d/workoutTracking/workouts"

# Headers
exercise_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

exercise_input = input("What exercise did you do?: ")

# Exercise parameters
exercise_params = {
    "query": exercise_input,
}

# Get Exercises data
exercise_response = requests.post(url=exercise_endpoint, json=exercise_params, headers=exercise_headers)
exercise_data = exercise_response.json()

# Sheety Section - Push data to Google Sheets
today = datetime.now().strftime("%m/%d/%Y")
time = datetime.now().time().strftime("%I:%M:%S %p")

sheety_headers = {
    "Authorization": f"Bearer {BEARER_TOKEN}"
}

for exercise in exercise_data["exercises"]:
    tracker_data = {
        "workout": {
            "date": today,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    sheety_update = requests.post(url=sheety_endpoint, json=tracker_data, headers=sheety_headers)




