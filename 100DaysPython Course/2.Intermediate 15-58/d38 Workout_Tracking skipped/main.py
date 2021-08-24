import json
import requests
from requests.api import post
from datetime import datetime

NUTRIONIX_API_KEY = "e7e32d387473bf7a9841e574d890f937"
NUTRIONIX_APP_ID = "77ef0eb4"

URL_POST_NATURAL_LANGUAGE="https://trackapi.nutritionix.com/v2/natural/exercise"
URL_SHEETY = " https://api.sheety.co/e5acd3a8ed7f93895d7d34fa8a86aebb/myWorkouts/workouts"



exercise_text =input("Tell me which exercises you did: ")

nutrix_headers={
  "x-app-id": NUTRIONIX_APP_ID,
  "x-app-key" : NUTRIONIX_API_KEY,
}

param = {
  "query": exercise_text,
  "gender": "male",
  "weight_kg": 60,
  "height_cm": 175,
  "age": 20
}

response = requests.post(URL_POST_NATURAL_LANGUAGE,headers=nutrix_headers, json=param)
result = response.json()


today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(URL_SHEETY, json=sheet_inputs)