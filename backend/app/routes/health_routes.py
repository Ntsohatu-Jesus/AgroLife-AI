from fastapi import APIRouter
from app.services.health_service import get_health_advice

router = APIRouter()

@router.get("/health")
def health_endpoint(symptom: str):
    return get_health_advice(symptom)