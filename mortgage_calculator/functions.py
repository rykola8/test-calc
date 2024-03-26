def calculate_monthly_payment(principal, annual_interest_rate, years):
    monthly_interest_rate = annual_interest_rate / 12 / 100
    months = years * 12
    monthly_payment = principal * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** -months)
    return monthly_payment