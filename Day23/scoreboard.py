from turtle import Turtle

class Scoreboard(Turtle):
    
    def __init__(self,screensize) -> None:
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(-abs(screensize[0]/2 - 30), abs(screensize[1]/2 - 30))

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}",align="center", font=('Arial', 12, 'normal'))
