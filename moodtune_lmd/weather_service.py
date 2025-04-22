# weather_service.py

import httpx
from config import settings

class WeatherAPIError(Exception):
    """Raised when weather API call fails"""
    pass

WEATHER_BASE_PARAMS = {
    "appid": settings.openweather_api_key,
    "units": "metric"
}

async def _call_weather_api(city: str) -> dict:
    """
    Internal helper to call OpenWeatherMap API with given city.
    """
    params = {**WEATHER_BASE_PARAMS, "q": city}

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(settings.openweather_url, params=params)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        raise WeatherAPIError(f"Weather API responded with {e.response.status_code}: {e.response.text}")
    except httpx.RequestError as e:
        raise WeatherAPIError(f"Weather API request failed: {str(e)}")

async def get_weather_by_city(city: str) -> dict:
    """
    Fetches weather 'main' and 'description' for a given city.
    """
    data = await _call_weather_api(city)

    try:
        weather = data["weather"][0]
        return {
            "main": weather["main"],
            "description": weather["description"]
        }
    except (KeyError, IndexError):
        raise WeatherAPIError("Malformed response from Weather API")

