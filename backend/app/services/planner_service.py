def generate_plan(activity: str, duration: str):
    activity = activity.lower()

    # 🌽 Farming plan
    if "farm" in activity or "plant" in activity:
        if duration == "weekly":
            return {
                "type": "Weekly Farming Plan",
                "plan": [
                    "Day 1: Clear land and prepare soil",
                    "Day 2: Gather seeds and tools",
                    "Day 3: Plant crops early morning or evening",
                    "Day 4: Water crops and check soil moisture",
                    "Day 5: Remove weeds manually",
                    "Day 6: Apply organic fertilizer if available",
                    "Day 7: Rest and monitor crop growth"
                ]
            }
        else:
            return {
                "type": "Daily Farming Plan",
                "plan": [
                    "Early morning: Inspect crops",
                    "Morning: Water plants if needed",
                    "Afternoon: Remove weeds",
                    "Evening: Check for pests or disease"
                ]
            }

    # 📚 Study plan
    elif "study" in activity:
        return {
            "type": "Daily Study Plan",
            "plan": [
                "Morning: Review previous notes",
                "Midday: Learn new topic",
                "Afternoon: Practice exercises",
                "Evening: Revise and summarize"
            ]
        }

    # 🧠 General fallback
    else:
        return {
            "message": "I can help create simple plans.",
            "suggestion": "Try 'farming', 'planting', or 'study'"
        }