# main.py

from fastapi import FastAPI, HTTPException, Request, Path
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from schemas import MoodWeatherRequest, MoodWeatherResponse, Song
from weather_service import *
from music_service import *
from aws_gateway import mood_match
from logger import logger


logger.info("Starting song recommendation application...")

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.post("/recommend-song", summary="Recommend Song Based on Mood & Weather",response_model=MoodWeatherResponse)
async def match_mood(request: MoodWeatherRequest):
    try:
        logger.info(f"Received mood match request: mood={request.mood}, city={request.city}")
        weather_data = await get_weather_by_city(request.city)
        weather = weather_data["main"] 
        weather_desc = weather_data["description"]
        logger.info(f"Weather API returned: {weather}, {weather_desc}")

    except WeatherAPIError as e:
        logger.error(f"Weather API error: {str(e)}")
        raise HTTPException(status_code=502, detail=f"Weather API Error: {str(e)}")
    
    lambda_result = mood_match(request.mood, weather, weather_desc)
    matched = lambda_result["match"]
    logger.info(f"Mood match result: matched={matched}")

    try:
        title, artist = await get_song_by_mood(request.mood)
        song = Song(title=title, artist=artist)
        logger.info(f"Recommended song: {title} by {artist}")
    except MusicAPIError as e:
        logger.error(f"Music API error: {str(e)}")
        song = None

    if matched:
        message = "Vibes aligned — enjoy your perfect Tune 🎧"
    else:
        message = "No need for weather approval — here’s your jam 🎧"

    return {
    "mood": request.mood,
    "weather_main": weather,
    "weather_description": weather_desc,
    "match": matched,
    "message": message,
    "song": song
}

@app.get("/weather/{city}", summary="Get Weather by City")
async def get_weather(city: str = Path(..., example="Delhi")):
    try:
        logger.info(f"Getting weather for city: {city}")
        return await get_weather_by_city(city)
    except WeatherAPIError as e:
        raise HTTPException(status_code=502, detail=f"Weather API Error: {str(e)}")


@app.get("/song/{query}", summary="Get Song by Title")
async def get_song(query: str = Path(..., example="Shape of You")):
    try:
        logger.info(f"Getting song for title: {query}")
        return await get_song_by_title(query)
    except MusicAPIError as e:
        raise HTTPException(status_code=502, detail=f"Music API Error: {str(e)}")


@app.get("/song/{tag}", summary="Get Song by Mood")
async def get_song_on_mood(tag: str = Path(..., example="happy")):
    try:
        logger.info(f"Getting song for mood: {tag}")
        return await get_song_by_mood(tag)
    except MusicAPIError as e:
        raise HTTPException(status_code=502, detail=f"Music API Error: {str(e)}")