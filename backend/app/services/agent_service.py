from app.services.weather_service import get_weather_data
from app.services.health_service import get_health_advice
from app.services.planner_service import generate_plan
from app.services.llm_service import generate_response

def handle_query(query: str):
    query_lower = query.lower()

    # 🌦 Weather
    if "weather" in query_lower:
        return get_weather_data("Bamenda")

    # 🏥 Health
    elif any(word in query_lower for word in ["snake", "cut", "burn", "fever"]):
        return get_health_advice(query)

    # 📅 Planner
    elif any(word in query_lower for word in ["plan", "schedule", "farm", "study"]):
        return generate_plan(query, "daily")

    # 🤖 LLM handles everything else
    else:
        ai_response = generate_response(
            f"You are AgroLife AI, an assistant for African farmers and communities. "
            f"Give practical, simple advice.\n\nUser: {query}"
        )

        return {
            "ai_response": ai_response
        }