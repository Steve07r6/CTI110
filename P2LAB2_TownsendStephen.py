# Stephen Townsend
# 6/20/2024
# P2LAB2
# write code that uses a dictionary to store user input and displays output to the user

mpg_dict = {
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26
}

keys = mpg_dict.keys()
print(keys)

vehicle = input("Enter a vehicle to see it's mpg: ")

if vehicle in mpg_dict:
    mpg = mpg_dict[vehicle]
    print(f"The {vehicle} gets: {mpg}")

    miles = float(input("How many miles you will drive?"))

    gallons_needed = miles / mpg

    print(f"{gallons_needed:.2f} gallons of gas are needed to drive the {vehicle} {miles} miles")
else:
    print("Vehicle not found in the dictionary.")
