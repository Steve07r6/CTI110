# Stephen Townsend
# 2024-06-20
# P2HW2
# Basic code to calculate statistics for test grades


module1 = float(input("Enter grade for Module 1: "))
module2 = float(input("Enter grade for Module 2: "))
module3 = float(input("Enter grade for Module 3: "))
module4 = float(input("Enter grade for Module 4: "))
module5 = float(input("Enter grade for Module 5: "))
module6 = float(input("Enter grade for Module 6: "))

lowest_grade = min(module1, module2, module3, module4, module5, module6)
highest_grade = max(module1, module2, module3, module4, module5, module6)
sum_grades = module1 + module2 + module3 + module4 + module5 + module6
average_grade = sum_grades / 6

print("\n---------- Grades Statistics ----------")
print(f"Lowest Grade:     {lowest_grade}")
print(f"Highest Grade:    {highest_grade}")
print(f"Sum of Grades:    {sum_grades}")
print(f"Average Grade:    {average_grade:.2f}")
print("--------------------------------------")

