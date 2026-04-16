from app.services.llm_service import generate_response

# Simple in-memory conversation storage
memory_store = {}

def smart_fallback(query: str):
    query = query.lower()

    # 🔥 General farming detection
    farming_keywords = [
        "plant", "grow", "harvest", "crop", "farm",
        "soil", "water", "fertilizer", "manure",
        "pest", "weed", "irrigation"
    ]

    if any(word in query for word in farming_keywords):
        return f"""Here is a practical farming guide based on your question:

1. Prepare land properly (clear weeds and loosen soil)
2. Use good quality seeds suited to your region
3. Plant at correct spacing depending on the crop
4. Water early morning or evening to reduce evaporation
5. Apply organic manure to improve soil fertility
6. Control pests using safe local methods (ash, neem, etc.)
7. Harvest at the right maturity stage

This method applies to crops like maize, tomatoes, rice, yam, cassava, and vegetables in African conditions."""

    # 🔥 Health-related fallback (optional but good for demo)
    if "cut" in query or "wound" in query:
        return """For a minor cut:

1. Clean the wound with clean water
2. Apply gentle pressure to stop bleeding
3. Use antiseptic if available
4. Cover with a clean cloth or bandage

Seek medical help if bleeding continues or infection appears."""

    if "snake" in query or "bite" in query:
        return """If bitten by a snake:

1. Stay calm and reduce movement
2. Do NOT cut or suck the wound
3. Keep the affected area still
4. Seek medical help immediately

Avoid traditional methods that may worsen the condition."""

    # 🔥 Default fallback
    return "I currently focus on farming and basic health advice. Please ask relevant questions."
def format_response(result):
    # If already a string → return directly
    if isinstance(result, str):
        return result

    # If dictionary → format nicely
    if isinstance(result, dict):

        # HEALTH RESPONSE
        if "advice" in result:
            advice_text = "\n".join([f"- {item}" for item in result["advice"]])
            return f"{result.get('condition', 'Health Advice')}:\n\n{advice_text}"

        # WEATHER RESPONSE
        if "temperature" in result:
            return (
                f"Weather in {result.get('location')}:\n"
                f"- Temperature: {result.get('temperature')}°C\n"
                f"- Condition: {result.get('description')}\n\n"
                f"This weather is generally suitable for farm activities, "
                f"but monitor rainfall and soil condition."
            )

        # PLANNER RESPONSE
        if "plan" in result:
            plan_text = "\n".join([f"- {item}" for item in result["plan"]])
            return f"{result.get('type', 'Farming Plan')}:\n\n{plan_text}"

    # Fallback (just convert to string)
    return str(result)

def run_agent(query: str, session_id: str = "default"):

    query_lower = query.lower()

    # 🔴 HEALTH FIRST
    if any(word in query_lower for word in [
        "snake", "bite", "cut", "injury", "wound", "blood",
        "pierce", "pain", "bleeding"
    ]):
        from app.services.health_service import get_health_advice
        result = get_health_advice(query)
        return {
            "response": str(result),
            "session_id": session_id
        }

    # 🌦 WEATHER
    if "weather" in query_lower:
        from app.services.weather_service import get_weather_data
        result = get_weather_data("Bamenda")
        return {
            "response": str(result),
            "session_id": session_id
        }

    # 📅 PLANNER
    if any(word in query_lower for word in ["plan", "schedule", "routine"]):
        from app.services.planner_service import generate_plan
        result = generate_plan("farming", "weekly")
        return {
            "response": str(result),
            "session_id": session_id
        }

    # 🌱 DEFAULT (AI)
    previous = memory_store.get(session_id, "")

    full_prompt = f"""
Previous conversation:
{previous}

Current question:
{query}
"""

    ai_response = generate_response(full_prompt)

    if not ai_response or not isinstance(ai_response, str):
        ai_response = smart_fallback(query)

    memory_store[session_id] = full_prompt + "\n" + ai_response

    return {
        "response": str(ai_response),
        "session_id": session_id
    }