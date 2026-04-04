from fastapi import FastAPI
from app.routes.weather_routes import router as weather_router

app = FastAPI()

app.include_router(weather_router)