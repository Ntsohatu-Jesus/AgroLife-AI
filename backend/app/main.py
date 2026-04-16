from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.weather_routes import router as weather_router
from app.routes.health_routes import router as health_router
from app.routes.agent_routes import router as agent_router
from app.routes.planner_routes import router as planner_router

app = FastAPI()

# 🔥 ADD THIS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(weather_router)
app.include_router(health_router)
app.include_router(agent_router)
app.include_router(planner_router)