from turtle import Turtle, Screen
import random

jimmy = Turtle()
color_list = ["red","green","blue","brown","yellow","pink","purple","medium aquamarine"]
screen = Screen()

full_angle = 360
angle_count = 3

jimmy.shape("turtle")
for angl in range(angle_count,11):
    color = random.choice(color_list)
    jimmy.color(color)
    for steps in range(angl):
        jimmy.forward(100)
        jimmy.right(full_angle/angl)
screen.exitonclick()
