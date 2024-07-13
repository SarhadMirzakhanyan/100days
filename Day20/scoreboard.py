from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    highscore_file = "./highscore.txt"
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}, Highscore: {self.highscore}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def read_highscore(self):
        with open(self.highscore_file) as f:
            self.highscore = f.read()
    
    def write_highscore(self):
        with open(self.highscore_file,"w") as f:
            f.write(str(self.highscore))

    def update_highscore(self):
        self.highscore = self.score
        self.write_highscore()

    def reset_score(self):
        if self.score > self.highscore:
            self.update_highscore()
        self.score = 0
        self.update_scoreboard()