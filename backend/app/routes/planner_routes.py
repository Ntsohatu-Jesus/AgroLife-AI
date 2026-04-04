from fastapi import APIRouter
from app.services.planner_service import generate_plan

router = APIRouter()

@router.get("/planner")
def planner_endpoint(activity: str, duration: str = "daily"):
    return generate_plan(activity, duration)