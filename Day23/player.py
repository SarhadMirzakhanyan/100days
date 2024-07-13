from turtle import Turtle

class Player(Turtle):

    def __init__(self, screensize, shape: str = "turtle") -> None:
        super().__init__(shape)
        # print(screensize[1]/2)
        self.screensize = screensize
        self.penup()
        self.goto(0,-abs(self.screensize[1]/2) + 20)
        self.seth(90)

    def hit_car(self, car_manager):
        for car in car_manager.cars:
            if abs(self.distance(car)) < 20:
                return True
            return False
        
    def move(self):
        self.forward(20)
    
    def go_next_lvl(self):
        self.goto(0,-abs(self.screensize[1]/2)+20)