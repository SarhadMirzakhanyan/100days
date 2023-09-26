import turtle
import random


jimmy = turtle.Turtle()
screen = turtle.Screen()
jimmy.shape("turtle")
jimmy.shapesize(1)
jimmy.speed(0)
turtle.colormode(255)

def random_color():
    r, g, b = [random.randint(0,255) for _ in range(3)]
    return (r,g,b)

for _ in range(360//6):
    jimmy.color(random_color())
    jimmy.circle(100)
    jimmy.right(6)



screen.exitonclick()