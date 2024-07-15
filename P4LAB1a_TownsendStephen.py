# Stephen Townsend
# 2024-07-06
# P4LAB1b
# turtle squares and triangles using loops


import turtle


t = turtle.Turtle()
t.speed(2)

side_length = 100
angle = 90
sides = 4

for _ in range(sides):
    t.forward(side_length)
    t.right(angle)

t.penup()  
t.goto(-50, -50)  
t.pendown()  

triangle_side_length = 100
triangle_angle = 120
triangle_sides = 3

for _ in range(triangle_sides):
    t.forward(triangle_side_length)
    t.left(triangle_angle)

turtle.done()
