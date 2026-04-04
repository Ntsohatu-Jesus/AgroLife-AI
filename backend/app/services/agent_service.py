from app.services.weather_service import get_weather_data
from app.services.health_service import get_health_advice
from app.services.planner_service import generate_plan

def handle_query(query: str):
    query_lower = query.lower()

    # 🌦 Weather intent
    if "weather" in query_lower:
        return get_weather_data("Bamenda")

    # 🏥 Health intent
    elif any(word in query_lower for word in ["snake", "cut", "burn", "fever"]):
        return get_health_advice(query)

    # 📅 Planning intent
    elif any(word in query_lower for word in ["plan", "schedule", "farm", "study"]):
        return generate_plan(query, "daily")

    # 🤖 Default response
    else:
        return {
            "message": "I can help with farming, health, and planning.",
            "examples": [
                "What is the weather today?",
                "I have a cut, what should I do?",
                "Give me a farming plan"
            ]
        }