import turtle
from math import floor
from random import randint


screen = turtle.Screen()
# screen.screensize(1000, 800)
screen.setup(width=1200, height=900)
screen.tracer(0)
screen.listen()
screen.colormode(255)

turtle_position = (0, -abs(screen.screensize()[1]))
print(turtle_position)
num_of_obs = floor(screen.window_height()/40)
print(screen.screensize())
loop_condition = True
obstacles = []
for i in range(num_of_obs):
    obstacle_obj = turtle.Turtle(shape="square")
    obstacle_obj.penup()
    obstacle_obj.shapesize(stretch_len=3, stretch_wid=1)
    obs_x_pos = randint(-abs(screen.screensize()[0]), screen.screensize()[0])
    obs_y_pos = -abs(screen.screensize()[1] + 20)+i*30
    obstacle_obj.color(tuple(randint(0, 255) for _ in range(3)))
    obstacle_obj.setpos(obs_x_pos, obs_y_pos)
    
    obstacles.append(obstacle_obj)

my_turtle = turtle.Turtle(shape="turtle")
my_turtle.penup()
my_turtle.seth(90)
my_turtle.setpos(turtle_position)
screen.update()
screen.exitonclick()

# while loop_condition:
