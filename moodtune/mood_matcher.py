# mood_matcher.py

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

class MoodMatcher:
    @classmethod
    def is_match(cls, mood: str, weather_main: str, weather_desc: str) -> bool:
        mood = mood.lower()
        weather_main = weather_main.capitalize()
        weather_desc = weather_desc.lower()

        if mood in POSITIVE_MOODS:
            if weather_main in POSITIVE_WEATHER:
                return True
        elif mood in NEGATIVE_MOODS:
            if weather_main in NEGATIVE_WEATHER:
                return True
        elif mood in NEUTRAL_MOODS:
            if weather_main in POSITIVE_WEATHER or weather_main in NEGATIVE_WEATHER:
                return True

        for keyword in MOOD_KEYWORDS.get(mood, []):
            if keyword in weather_desc:
                return True

        return False


