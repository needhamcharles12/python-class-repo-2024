#!/usr/bin/env python3

print("Investment Calculator\n")

investment_amount = int(input("Please enter your investment amount. (greater than 0 and less than 50,000): "))
while investment_amount <= 0 or investment_amount > 50000:
    print("Amount is out of range. Please try again.")
    investment_amount = int(input("Please enter your investment amount. (greater than 0 and less than 50,000): "))
    

interest_rate = int(input("Please enter the interest rate. (greater than 0 and less than 15): "))
while interest_rate < 0 or interest_rate > 15:
    print("Amount is out of range. Please try again.")
    interest_rate = int(input("Please enter the interest rate. (greater than 0 and less than 15): "))


investment_duration = int(input("Please enter the investment duration in years. (greater than 0): "))
while investment_duration <= 0:
    print("Amount is out of range. Please try again.")
    investment_duration = int(input("Please enter the investment duration in years. (greater than 0): "))

future_value = 0

monthly_rate = interest_rate / 12 / 100


print("")

if investment_duration > 0:     #if-statement to check if the current month loop is for a full year
    for year in range(investment_duration):     #Outer loop is how many years the loop will run
        for month in range(12):                      #Nested inner loop runs the calculation each month for a year
            future_value += investment_amount
            monthly_interest = future_value * monthly_rate
            future_value += monthly_interest
        print(f"Year {year + 1}: ${round(future_value, 2)}")    #Print statement for each year


print()

print(f"Investment duration: {investment_duration} years")
print(f"Yearly interest rate: {interest_rate}%")
print(f"Monthly investment amount: ${investment_amount}")
print(f"Your total investment: ${round(future_value, 2)}")
print("")
print("------------------------------------------")
print("Coded by Charles Needham")














