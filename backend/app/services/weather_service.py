import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")

def get_weather_data(location: str):
    if not API_KEY:
        return {"error": "API key not found"}

    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)

        if response.status_code != 200:
            return {"error": "Could not fetch weather data"}

        data = response.json()

        return {
            "location": location,
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"]
        }

    except Exception as e:
        return {"error": str(e)}

print("API KEY:", API_KEY)