import turtle
import random

colors = [(197, 166, 114), (64, 102, 124), (147, 166, 182), (14, 41, 59), (223, 205, 125), (142, 85, 57), (130, 77, 93), (183, 152, 165), (147, 174, 156), (71, 108, 89), (174, 148, 57), (17, 47, 38), (177, 99, 116), (123, 39, 30), (25, 88, 66), (72, 37, 26)]
jimmy = turtle.Turtle()
screen = turtle.Screen()
step_size = 50

screen.canvwidth = 400
screen.canvheight = 400
turtle.colormode(255)

jimmy.penup()
jimmy.hideturtle()
jimmy.setx(-200)
jimmy.sety(-200)

#jimmy.shape("circle")
jimmy.shapesize(1)
jimmy.speed(8)

for i in range(10):
    for j in range(10):
        jimmy.dot(20,random.choice(colors))
        jimmy.forward(step_size)
    jimmy.setx(-200)
    jimmy.sety(jimmy.ycor() + step_size)

        

screen.exitonclick()