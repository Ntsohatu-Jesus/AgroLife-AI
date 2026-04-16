def get_health_advice(query: str):

    query = query.lower()

    if "cut" in query or "bleeding" in query or "pierce" in query:

        return """First Aid for a Cut or Injury:

1. Wash your hands if possible
2. Clean the wound with clean water
3. Apply pressure with a clean cloth to stop bleeding
4. Apply antiseptic if available
5. Cover with a clean bandage or cloth

Seek medical help if bleeding continues or signs of infection appear.
"""

    if "snake" in query or "bite" in query:

        return """Snake Bite First Aid:

1. Stay calm and reduce movement
2. Keep the affected area still
3. Do NOT cut or suck the wound
4. Remove tight clothing or jewelry
5. Seek medical help immediately

Avoid using traditional methods that may worsen the condition.
"""

    return "Please describe the injury clearly (e.g., cut, burn, snake bite)."