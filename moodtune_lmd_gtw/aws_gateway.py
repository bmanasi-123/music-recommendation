import requests
from config import settings

def mood_match(mood: str, weather_main: str, weather_description: str) -> dict:
    url = settings. api_url + settings.api_route  

    payload = {
        "mood": mood,
        "weather_main": weather_main,
        "weather_description": weather_description
    }

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print("[ERROR] API Gateway call failed:", e)
        return {"match": False, "message": "Failed to get mood match from API Gateway"}
