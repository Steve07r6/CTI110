# Stephen Townsend
# 6/20/2024
# P2LAB1
# Basic code in Python to calculate different variables in a circle

import math

radius = float(input("What is the radius of the circle?"))

diameter = 2 * radius
circumference = 2 * math.pi * radius
area = math.pi * radius ** 2

formatted_diameter = format(diameter, ".1f")  
formatted_circumference = format(circumference, ".2f")  
formatted_area = format(area, ".3f")  

print(f"The diameter of the circle is {formatted_diameter}")
print(f"The circumference of the circle is {formatted_circumference}")
print(f"The area of the circle is {formatted_area}")
