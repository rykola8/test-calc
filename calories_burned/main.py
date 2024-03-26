from functions import calculate_calories_burned

print("Welcome to the Calories Burned Calculator!")
activity = input("Enter the activity (e.g., running, cycling, swimming): ")
duration = float(input("Enter the duration of activity in minutes: "))
weight = float(input("Enter your weight in kilograms: "))
calories_burned = calculate_calories_burned(activity, duration, weight)

if isinstance(calories_burned, str):
    print(calories_burned)
else:
    print("You burned calories.", calories_burned)