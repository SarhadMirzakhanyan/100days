import turtle
import random

rotations = [0, 90, 180, 270]
colors = ["red","green","blue","brown","yellow","pink","purple","medium aquamarine"]
jimmy = turtle.Turtle()
jimmy.pensize(6)
screen = turtle.Screen()
turtle.colormode(255)

def random_color():
    r, g, b = [random.randint(0,255) for _ in range(3)]
    return (r,g,b)

for _ in range(200):
    jimmy.color(random_color())
    jimmy.forward(30)


    jimmy.right(random.choice(rotations))

screen.exitonclick()