# Stephen Townsend
# 2024-07-06
# P4LAB2
# multiplying an integer with a loop

def display_multiplication_table(number):
    print(f"Multiplication Table for {number}:")
    for i in range(1, 13):
        print(f"{number} * {i} = {number * i}")

def main():
    while True:
        user_input = input("Enter an integer: ")
        
        if user_input.lower() == "no":
            print("Exiting program...")
            break
        
        try:
            number = int(user_input)
            
            if number < 0:
                print("This program does not handle negative numbers.")
            else:
                display_multiplication_table(number)
        except ValueError:
            print("Would you like to run the program again?")
        
        run_again = input("Would you like to run the program again? ")
        if run_again.lower() != "yes":
            print("Exiting program...")
            break

if __name__ == "__main__":
    main()
