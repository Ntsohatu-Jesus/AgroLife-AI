def generate_plan(activity="farming", duration="weekly"):

    if duration == "weekly":

        return """Weekly Farming Plan:

Day 1: Clear land and prepare soil  
Day 2: Gather seeds and tools  
Day 3: Plant crops (morning/evening)  
Day 4: Water crops and monitor soil  
Day 5: Remove weeds  
Day 6: Apply manure or fertilizer  
Day 7: Rest and observe crop growth  
"""

    if duration == "monthly":

        return """Monthly Farming Plan:

Week 1: Land clearing and preparation  
Week 2: Planting and early watering  
Week 3: Weeding and pest control  
Week 4: Fertilizing and monitoring growth  

Harvest depending on crop maturity.
"""

    return "Please specify plan duration (weekly or monthly)."