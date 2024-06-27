# Stephen Townsend
# 6/26/2024
# P3LAB
# This program calculates the minimum number of dollars, quarters, dimes, nickels, and pennies needed to make up a given amount of money.

money = float(input('Enter the amount of money: '))
total_cents = int(money * 100)
dollars = total_cents // 100
total_cents %= 100
quarters = total_cents // 25
total_cents %= 25
dimes = total_cents // 10
total_cents %= 10
nickels = total_cents // 5
total_cents %= 5
pennies = total_cents

if dollars > 0:
    print(f'Dollars: {"1 dollar" if dollars == 1 else f"{dollars} dollars"}')
if quarters > 0:
    print(f'Quarters: {"1 quarter" if quarters == 1 else f"{quarters} quarters"}')
if dimes > 0:
    print(f'Dimes: {"1 dime" if dimes == 1 else f"{dimes} dimes"}')
if nickels > 0:
    print(f'Nickels: {"1 nickel" if nickels == 1 else f"{nickels} nickels"}')
if pennies > 0:
    print(f'Pennies: {"1 penny" if pennies == 1 else f"{pennies} pennies"}')
