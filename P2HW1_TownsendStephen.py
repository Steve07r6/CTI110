# Stephen Townsend
# 6/20/2024
# P2HW1
# Basic code for travel expenses

budget = float(input("Enter Budget: "))
destination = input("Enter your travel destination: ")
gas_expense = float(input("How much do you think you will spend on gas? "))
accommodation_expense = float(input("Approximately, how much will you need for accommodation/hotel? "))
food_expense = float(input("How much do you need for food? "))

print("----------Travel Expenses----------")
print(f"Location:         {destination}")
print(f"Fuel:             ${gas_expense:8.2f}")
print(f"Accommodation:    ${accommodation_expense:8.2f}")
print(f"Food:             ${food_expense:8.2f}")
print("-----------------------------------")
