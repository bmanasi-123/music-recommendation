from mood_matcher import MoodMatcher

def test_basic_mood_weather_match():
    assert MoodMatcher.is_match("happy", "Clear", "clear sky") is True
    assert MoodMatcher.is_match("sad", "Sunny", "bright sunlight") is False
    assert MoodMatcher.is_match("chill", "Mist", "misty morning") is True
    assert MoodMatcher.is_match("nonexistent", "Clear", "clear sky") is False

def test_case_insensitivity():
    assert MoodMatcher.is_match("HAPPY", "clear", "clear sky") is True
    assert MoodMatcher.is_match("ChIlL", "mist", "misty morning") is True

def test_keyword_fallback_match():
    assert MoodMatcher.is_match("nostalgic", "Sunny", "light rain and fog") is True
    assert MoodMatcher.is_match("romantic", "Clouds", "sunset breeze") is True

def test_no_match():
    assert MoodMatcher.is_match("happy", "Rain", "heavy rain") is False
    assert MoodMatcher.is_match("excited", "Fog", "dense fog") is False
