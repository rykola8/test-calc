from functions import calculate_monthly_payment

print("Welcome to the Mortgage Calculator!")
amount = float(input("Enter the loan amount: "))
annual_interest_rate = float(input("Enter the annual interest rate (e.g., 5 for 5%): "))
years = int(input("Enter the loan term in years: "))

monthly_payment = calculate_monthly_payment(amount, annual_interest_rate, years)

print("\nYour monthly payment will be: €{:.2f}".format(monthly_payment))