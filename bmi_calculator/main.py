from functions import calculate_bmi, interpret_bmi

print("Welcome to the BMI Calculator!")
weight_kg = float(input("Enter your weight in kilograms: "))
height_m = float(input("Enter your height in meters: "))
bmi = calculate_bmi(weight_kg, height_m)
interpretation = interpret_bmi(bmi)
print("Your BMI is {:.2f}".format(bmi))
print("Interpretation: ", interpretation)