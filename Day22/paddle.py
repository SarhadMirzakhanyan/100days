from turtle import Turtle

PADDLE_HEIGHT = 4
PADDLE_COLOR = "white"


class Paddle(Turtle):

    def __init__(self, pos, screensize, shape: str = "square", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.shapesize(stretch_wid=PADDLE_HEIGHT, stretch_len=1)
        self.penup()
        self.color(PADDLE_COLOR)
        if pos == "left":
            self.goto((screensize[0]/2 - 20)*-1, 0)
        elif pos == "right":
            self.goto(screensize[0]/2 - 20, 0)

    def move_up(self):
        if self.ycor() < 280:
            self.goto(self.xcor(), self.ycor() + 20)
        else:
            pass
    
    def move_down(self):
        if self.ycor() > -280:
            self.goto(self.xcor(), self.ycor() - 20)
        else:
            pass

