from turtle import Turtle

FONT=("Arial","12","normal")
ALIGNMENT = "center"

class Scoreboard(Turtle):
    def __init__(self,heigth) -> None:
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto((0,heigth//2 - 20))
    
    def add_to_score(self):
        self.score += 1
        self.clear()
        self.show_score()
    
    def show_score(self):
        self.write(f"Score: {self.score}",align=ALIGNMENT,font=FONT)

    
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align=ALIGNMENT,font=FONT)

    def __repr__(self) -> str:
        return f"The score is {self.score}"
    