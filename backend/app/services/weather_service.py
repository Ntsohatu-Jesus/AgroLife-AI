import requests
import os

API_KEY = os.getenv("WEATHER_API_KEY")

def get_weather_data(city="Bamenda"):

    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url).json()

        temp = response["main"]["temp"]
        desc = response["weather"][0]["description"]

        advice = ""

        if "rain" in desc:
            advice = "It may rain. Consider postponing farm activities."
        elif "clear" in desc or "sun" in desc:
            advice = "Weather is good for farming activities."
        else:
            advice = "Weather is moderate. You can proceed with caution."

        return f"""Weather Report for {city}:

Temperature: {temp}°C
Condition: {desc}

Advice: {advice}
"""

    except:
        return "Unable to fetch weather data at the moment."