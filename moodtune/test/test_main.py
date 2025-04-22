import pytest
from httpx import AsyncClient, ASGITransport
from main import app

@pytest.mark.asyncio
async def test_recommend_song_success():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.post("/recommend-song", json={
            "mood": "happy",
            "city": "London"
        })
        assert response.status_code == 200
        data = response.json()
        assert "mood" in data
        assert "weather_main" in data
        assert "weather_description" in data
        assert "match" in data
        assert "message" in data
        assert "song" in data

@pytest.mark.asyncio
async def test_recommend_song_weather_failure():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.post("/recommend-song", json={
            "mood": "happy",
            "city": "InvalidCity123"
        })
        assert response.status_code == 502
        data = response.json()
        assert "detail" in data

@pytest.mark.asyncio
async def test_get_weather_by_city():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.get("/weather/Paris")
        assert response.status_code == 200
        data = response.json()
        assert "main" in data
        assert "description" in data

@pytest.mark.asyncio
async def test_get_song_by_title():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.get("/song/Shape of You")
        assert response.status_code == 200
        data = response.json()
        assert "title" in data
        assert "artist" in data

@pytest.mark.asyncio
async def test_get_song_by_mood():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.get("/song/happy")
        assert response.status_code == 200
        data = response.json()
        assert "title" in data
        assert "artist" in data
