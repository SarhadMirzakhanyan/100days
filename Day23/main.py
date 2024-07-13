import turtle
from time import sleep
from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard
from random import randint

SCREEN_SIZE = (910, 600)
screen = turtle.Screen()
screen.setup(width=SCREEN_SIZE[0],height=SCREEN_SIZE[1])
# screen.screensize(SCREEN_SIZE[0]+100, SCREEN_SIZE[1]+100)
screen.tracer(0)
screen.listen()
screen.colormode(255)
print(f" Screensize is: {screen.screensize()}")
print(f"Screen windows size is: height {screen.window_height()}, width {screen.window_width()}")


mycar = Player(SCREEN_SIZE)
car_manager = CarManager(SCREEN_SIZE)
scoreboard = Scoreboard(screensize=SCREEN_SIZE)
scoreboard.update_score()
screen.update()

screen.onkey(mycar.move,"Up")
loop_condition = True
while loop_condition:
    sleep(0.1)
    if randint(1,6) == 6:
        car_manager.generate_car()
    car_manager.move_cars()
    screen.update()
    for car in car_manager.cars:
        if mycar.distance(car) < 20:
            loop_condition = False
    if mycar.ycor() == (SCREEN_SIZE[1]/2 - 20):
        mycar.go_next_lvl()
        car_manager.increase_speed()
        scoreboard.update_score()

screen.exitonclick()

# while loop_condition:
