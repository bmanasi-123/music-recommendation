# music_service.py

import httpx
from config import settings

class MusicAPIError(Exception):
    """Raised when the music API call fails"""
    pass

LASTFM_BASE_PARAMS = {
    "api_key": settings.lastfm_api_key,
    "format": "json"
}

async def _call_lastfm_api(extra_params: dict) -> dict:
    """
    Internal utility to call the Last.fm API with given method-specific params.
    """
    params = {**LASTFM_BASE_PARAMS, **extra_params}
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(settings.lastfm_url, params=params)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        raise MusicAPIError(f"Last.fm API returned {e.response.status_code}: {e.response.text}")
    except httpx.RequestError as e:
        raise MusicAPIError(f"Last.fm request failed: {str(e)}")

async def get_song_by_mood(mood: str) -> tuple[str, str]:
    """
    Fetches a song (title, artist) based on the mood tag using Last.fm.
    """
    data = await _call_lastfm_api({
        "method": "tag.gettoptracks",
        "tag": mood
    })

    try:
        top_track = data["tracks"]["track"][0]
        title = top_track["name"]
        artist = top_track["artist"]["name"]
        return title, artist
    except (KeyError, IndexError):
        raise MusicAPIError("No song found for the given mood")

async def get_song_by_title(query: str) -> dict:
    """
    Searches a track by title using Last.fm's track.search.
    """
    data = await _call_lastfm_api({
        "method": "track.search",
        "track": query,
        "limit": 1
    })

    try:
        top_track = data["results"]["trackmatches"]["track"][0]
        return {
            "title": top_track["name"],
            "artist": top_track["artist"],
            "url": top_track["url"]
        }
    except (KeyError, IndexError):
        raise MusicAPIError("No song found for the search query")
