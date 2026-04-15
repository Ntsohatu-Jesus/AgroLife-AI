def generate_response(prompt: str):
    prompt_lower = prompt.lower()

    # 🌽 MAIZE + WATERING
    if "maize" in prompt_lower and "water" in prompt_lower:
        return """For maize watering in dry season:

- Water 2–3 times per week depending on heat
- Water early morning (6–8am) or evening (5–7pm)
- Avoid watering under strong sun
- Use mulch (grass/leaves) to retain moisture
- Young maize needs more frequent watering

This helps maintain soil moisture in dry African conditions.
"""

    # 🌽 GENERAL MAIZE FARMING
    elif "maize" in prompt_lower:
        return """To grow maize in dry season:

1. Use early maturing seeds
2. Plant when soil still has moisture
3. Apply manure or compost
4. Use mulch to reduce water loss
5. Space crops properly (75cm rows)

This method is practical for farmers in dry regions of Africa.
"""

    # 🍅 TOMATO
    elif "tomato" in prompt_lower:
        return """To grow tomatoes successfully:

- Use raised beds
- Water regularly but not excessively
- Add compost or poultry manure
- Stake plants for support
- Remove infected leaves early
"""

    # 🌧 WEATHER
    elif "rain" in prompt_lower or "weather" in prompt_lower:
        return """Rainfall affects farming by:

- Improving soil moisture
- Supporting crop growth
- But too much rain can cause flooding

Farmers should adjust planting based on rainfall patterns.
"""

    # ❌ DEFAULT
    return "I currently focus on farming and basic health advice. Please ask about crops, weather, or farm-related issues."