from turtle import Turtle

class Ball(Turtle):
    x_step = 10
    y_step = 10

    def __init__(self, shape: str = "circle", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.penup()
        self.color("white")
        self.seth(45)

    def move(self):
        new_x = self.xcor() + self.x_step
        new_y = self.ycor() + self.y_step
        self.goto(new_x,new_y)

        if abs(self.ycor()) >= 280:
            self.bounce_y()

    def bounce_y(self):
        self.y_step *= -1
    
    def bounce_x(self):
        self.x_step *= -1
    
    def hit_paddle(self, paddle_obj) -> bool:
        if abs(self.xcor() - paddle_obj.xcor()) < 20 and abs(self.ycor() - paddle_obj.ycor()) < 50:
            print("returning true")
            return True