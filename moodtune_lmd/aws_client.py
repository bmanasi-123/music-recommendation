import boto3
import json

lambda_client = boto3.client("lambda", region_name="ap-southeast-2")  

def mood_match(mood: str, weather_main: str, weather_description: str):
    payload = {
        "mood": mood,
        "weather_main": weather_main,
        "weather_description": weather_description
    }

    response = lambda_client.invoke(
        FunctionName="moodmatcher",  
        InvocationType="RequestResponse",
        Payload=json.dumps(payload),
    )

    raw = json.load(response["Payload"])
    body = json.loads(raw.get("body", "{}")) 
    return body

