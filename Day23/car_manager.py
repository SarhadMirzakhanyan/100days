from turtle import Turtle
from random import randint
from math import floor

class CarManager():
    move_distance = 5
    def __init__(self,screensize) -> None:
        self.screensize = screensize
        self.cars = []


    def generate_car(self):
        car = Turtle(shape="square")
        car.penup()
        car.seth(180)
        car.shapesize(stretch_wid=1,stretch_len=2)
        rand_color = tuple(randint(0,255) for _ in range(3))
        y_pos = randint(-abs(self.screensize[1]/2)+40, abs(self.screensize[1]/2) - 40)
        x_pos = self.screensize[0]/2-20
        car.color(rand_color)
        car.setpos(x_pos, y_pos)
        self.cars.append(car)
    
    def increase_speed(self):
        self.move_distance += 5
    
    def move_cars(self):
        for car in self.cars:
            car.forward(self.move_distance)
            if car.xcor() < -abs(self.screensize[0]/2):
                car.hideturtle()
                self.cars.remove(car)