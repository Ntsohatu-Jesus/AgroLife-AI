from fastapi import FastAPI
from app.routes.weather_routes import router as weather_router
from app.routes.health_routes import router as health_router

app = FastAPI()

app.include_router(weather_router)
app.include_router(health_router)