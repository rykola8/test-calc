from functions import calculate_monthly_payment

print("Welcome to the Mortgage Calculator!")
amount = float(input("Enter the loan amount: "))
annual_interest_rate = float(input("Enter the annual interest rate (e.g., 5 for 5%): "))
years = int(input("Enter the loan term in years: "))

monthly_payment = calculate_monthly_payment(amount, annual_interest_rate, years)

print("\nYour monthly payment will be: €{:.2f}".format(monthly_payment))

#test plan
#hapy path
#lietotājs ievada aizdevuma summu eiro (500eur), gada procentus (5), ilgumu gados (2 gadi), un lietotājs iegūst summu, kas viņam jāmaksā katru mēnesi = 21,94 eiro.

#use case
#1.  