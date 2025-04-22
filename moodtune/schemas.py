# schemas.py

from pydantic import BaseModel , Field
from typing import Optional


class MoodWeatherRequest(BaseModel):
    mood: str
    city: str

    class Config:
        json_schema_extra = {
            "examples": [
                {
                    "mood": "happy",
                    "city": "London"
                }
            ]
        }


class Song(BaseModel):
    title: str
    artist: str


class MoodWeatherResponse(BaseModel):
    mood: str
    weather_main: str
    weather_description: str
    match: bool
    message: str 
    song: Optional[Song] = None
