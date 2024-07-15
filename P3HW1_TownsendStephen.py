
# Stephen Townsend
# 6/26/2024
# P3HW1
# Basic code to show the average grade for students



mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]


low = min(grades)
high = max(grades)
sum_grades = sum(grades)
avg = sum_grades / len(grades)


print("-------------Results-----------------")
print(f'Lowest grade: {low}')
print(f'Highest grade: {high}')
print(f'Sum of grades: {sum_grades}')
print(f'Average grade: {avg}')
print("-------------------------------------")

if avg >= 90:
    print('Your grade is: A')
elif avg >= 80:
    print('Your grade is: B')
elif avg >= 70:
    print('Your grade is: C')
elif avg >= 60:
    print('Your grade is: D')
else:
    print('Your grade is: F')
