from fastapi import APIRouter
from app.services.weather_service import get_weather_data

router = APIRouter()

@router.get("/weather")
def fetch_weather(location: str):
    return get_weather_data(location)