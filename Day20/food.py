from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self,window_size):
        self.window_size = window_size
        super().__init__()
        self.color("blue")
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.speed("fastest")
        self.recreate()
        
    
    def recreate(self):
        self.x_location_map = range(-abs(self.window_size[0]//2 - 20),abs(self.window_size[0]//2 - 20))
        self.y_location_map = range(-abs(self.window_size[1]//2 - 20),abs(self.window_size[1]//2 - 20))

        food_location = (random.choice(self.x_location_map), random.choice(self.y_location_map))

        self.goto(food_location)

