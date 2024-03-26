def calculate_calories_burned(activity, duration, weight):
    activities = {
        "running": 10,  # Calories burned per minute for running
        "cycling": 8,   # Calories burned per minute for cycling
        "swimming": 7,  # Calories burned per minute for swimming
        # Add more activities and their respective calorie burn rates here
    }

    if activity.lower() in activities:
        calories_burned_per_minute = activities[activity.lower()]
        total_calories_burned = calories_burned_per_minute * duration * (weight / 60)  # Adjust for weight
        return total_calories_burned
    else:
        return "Activity not found. Please choose from: " + ", ".join(activities.keys())
