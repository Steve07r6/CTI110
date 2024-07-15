# Stephen Townsend
# 2024-07-06
# P4LAB1b
# make initials using turtle 


import turtle

t = turtle.Turtle()
t.speed(1)  
t.pensize(3)  


t.penup()
t.goto(0, -100)  
t.pendown()
t.color("blue")
t.right(90)  
t.circle(50, 180)  
t.right(180)  
t.circle(50, -180)  


t.penup()
t.goto(50, 0)
t.pendown()
t.color("green")
t.right(90)
t.forward(100)
t.penup()
t.goto(100, 0)
t.pendown()
t.right(90)
t.forward(50)


t.hideturtle()
turtle.done()
