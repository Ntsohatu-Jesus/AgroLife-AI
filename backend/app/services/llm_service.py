def generate_response(prompt: str):
    # TEMP MOCK RESPONSE (no API dependency)

    if "maize" in prompt.lower():
        return """To grow maize in dry season:

1. Use early maturing seeds
2. Water in morning or evening
3. Apply manure to retain moisture
4. Use mulch (grass/leaves)
5. Space crops properly (75cm rows)

This method is practical for farmers in dry regions of Africa.
"""

    if "tomato" in prompt.lower():
        return """To grow tomatoes successfully:

1. Use raised beds
2. Water regularly but not too much
3. Add compost or poultry manure
4. Stake plants for support
5. Watch for pests and remove affected leaves
"""

    return "General advice: ensure proper watering, good soil, and pest control."