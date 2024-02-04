from turtle import  Turtle

class Scoreboard(Turtle):

    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.l_points = 0
        self.r_points = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.update_score()

    def update_score(self):
        self.goto(80,250)
        self.write(arg=self.r_points, font=("",24,""))
        self.goto(-80,250)
        self.write(arg=self.l_points, font=("",24,""))

    def point_left(self):
        self.l_points += 1
        self.clear()
        self.update_score()
     
    def point_right(self):
        self.r_points += 1
        self.clear()
        self.update_score()
