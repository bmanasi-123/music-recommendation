import json

POSITIVE_WEATHER = {"Clear", "Sunny", "Wind", "Clouds"}
NEGATIVE_WEATHER = {"Rain", "Drizzle", "Thunderstorm", "Fog", "Mist"}

POSITIVE_MOODS = {"happy", "excited", "motivated", "inspired"}
NEGATIVE_MOODS = {"sad", "lonely", "melancholy", "anxious"}
NEUTRAL_MOODS = {"chill", "calm", "lazy", "romantic", "moody", "nostalgic"}

MOOD_KEYWORDS = {
    "happy": ["clear", "sun", "bright"],
    "sad": ["rain", "storm", "drizzle"],
    "calm": ["cloud", "mist", "gentle"],
    "lazy": ["fog", "cloud", "hazy"],
    "excited": ["clear", "wind", "sunny"],
    "romantic": ["rain", "sunset", "breeze"],
    "moody": ["cloud", "fog", "overcast"],
    "nostalgic": ["fog", "rain", "cloud"],
    "lonely": ["drizzle", "grey", "mist"]
}

def lambda_handler(event, context):
    if "body" in event and isinstance(event["body"], str):
        try:
            data = json.loads(event["body"])
        except json.JSONDecodeError:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Invalid JSON format"})
            }
    else:
        data = event  

    mood = data.get("mood", "").lower()
    weather_main = data.get("weather_main", "").capitalize()
    weather_desc = data.get("weather_description", "").lower()

    # Match logic as before...
    matched = False
    if mood in POSITIVE_MOODS and weather_main in POSITIVE_WEATHER:
        matched = True
    elif mood in NEGATIVE_MOODS and weather_main in NEGATIVE_WEATHER:
        matched = True
    elif mood in NEUTRAL_MOODS and (weather_main in POSITIVE_WEATHER or weather_main in NEGATIVE_WEATHER):
        matched = True

    if not matched:
        for keyword in MOOD_KEYWORDS.get(mood, []):
            if keyword in weather_desc:
                matched = True
                break

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({"match": matched})
    }
