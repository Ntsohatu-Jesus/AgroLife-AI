from fastapi import APIRouter
from app.services.agent_service import handle_query

router = APIRouter()

@router.get("/agent")
def agent_endpoint(query: str):
    return handle_query(query)