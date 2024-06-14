# Stephen Townsend
# 6/12/2024
# P1HW1
# This is a basic python code text for adding and subtracting numbers

# Prompt the user to enter an integer as the base value
base = int(input("-----Calculating Exponents----\nEnter an integer as the base value: "))

# Prompt the user to enter an integer as the exponent
exponent = int(input("Enter an integer as the exponent: "))

# Calculate the result of base raised to the exponent
result = base ** exponent

# Print the result with proper formatting
print(f"\n{base} raised to the power of {exponent} is {result}!!")

# Prompt the user to enter three separate integers
num1 = int(input("-----Addition and Subtraction----\nEnter a starting integer: "))
num2 = int(input("Enter an integer to add: "))
num3 = int(input("Enter an integer to subtract: "))

# Calculate the sum of the first two integers
sum_of_first_two = num1 + num2

# Subtract the third integer from the sum of the first two
final_result = sum_of_first_two - num3

# Print the final result with proper formatting
print(f"\n{num1} + {num2} - {num3} is equal to {final_result}.")
