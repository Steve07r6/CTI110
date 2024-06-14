# Stephen Townsend
# 6/13/2024
# Travel Budget Calculator
# This program calculates the remaining budget after expenses for a travel trip.

# Ask user to enter their budget
budget = float(input("Enter budget: $"))

# Ask user to enter travel destination
destination = input("Enter your travel destination: ")

# Ask user for amount they will spend on gas
gas_expense = float(input("How much do you think you will spend on gas: $"))

# Ask user for amount they will spend on accommodation
accommodation_expense = float(input("Approximately, how much will you need for accommodation/hotel?: $"))

# Ask user for amount they will spend on food
food_expense = float(input("Last, how much do you need for food?: $"))

# Add expenses
total_expenses = gas_expense + accommodation_expense + food_expense

# Subtract expenses from budget
remaining_budget = budget - total_expenses

# Display results
print("\n-----------Travel Expenses----------")
print("Location:", destination)
print("Initial Budget: $", budget)
print("Fuel: $", gas_expense)
print("Accommodation: $", accommodation_expense)
print("Food: $", food_expense)
print("Total Expenses: $", total_expenses)
print("Remaining Balance: $", remaining_budget)
