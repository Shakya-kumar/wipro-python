# ------------------------------------------------------------------------------------
# Project 1: Travel Suggestion Based on Distance
#
# Create a Python program that asks the user how far they want to travel.
# - If they want to travel less than 3 miles, tell them to ride a Bicycle.
# - If they want to travel more than 3 miles but less than 300 miles, 
#   tell them to ride a Motor Cycle.
# - If they want to travel 300 miles or more, tell them to drive a Super-Car.
#
# Sample Output:
# How far would you like to travel in miles? 2500
# I suggest Super-Car to your destination
# ------------------------------------------------------------------------------------

distance = float(input("How far would you like to travel in miles? "))

if distance < 3:
    print("I suggest Bicycle to your destination")
elif distance < 300:
    print("I suggest Motor Cycle to your destination")
else:
    print("I suggest Super-Car to your destination")


# ------------------------------------------------------------------------------------
# Project 2: Cloud Server Cost Estimator
#
# Let’s assume you are planning to use your Python skills to build a PBLApp for Mo.
# You decide to host your application on servers running in the cloud.
# You pick a hosting provider that charges $50.51 per hour.
#
# You will launch your service using one server and want to know:
# - How much it will cost to operate one server per day?
# - How much it will cost to operate one server per week?
# - How much it will cost to operate one server per month?
# - How many days can one server run with a budget of $59,187?
#
# Sample Output:
# Cost to operate one server:
# Per Day: $1212.24
# Per Week: $8485.68
# Per Month: $36367.20
# Enter your budget in USD: 59187
# You can operate one server for approximately 48.82 days with $59187
# ------------------------------------------------------------------------------------
hourly_rate = 50.51
cost_per_day = hourly_rate * 24
cost_per_week = cost_per_day * 7
cost_per_month = cost_per_day * 30
print("\nCost to operate one server:")
print(f"Per Day: ${cost_per_day:.2f}")
print(f"Per Week: ${cost_per_week:.2f}")
print(f"Per Month: ${cost_per_month:.2f}")
budget = float(input("Enter your budget in USD: "))
days_possible = budget / cost_per_day
print(f"You can operate one server for approximately {days_possible:.2f} days with ${budget}")
