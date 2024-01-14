STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
SNAKE_STEP = 20


import turtle

class Snake():
    def __init__(self):
        self.snake_bites = []
        snake_head = turtle.Turtle(shape="triangle")
        snake_head.color("green")
        snake_head.penup()
        snake_head.goto(STARTING_POSITIONS[0])
        self.snake_bites.append(snake_head)
        for pos in STARTING_POSITIONS[1:]:
            snake = turtle.Turtle("square")
            snake.color("white")
            snake.penup()
            snake.goto(pos)
            self.snake_bites.append(snake)
    
    def move(self):
        for i in range(len(self.snake_bites) - 1, 0,-1):
            self.snake_bites[i].goto(self.snake_bites[i-1].pos())
        self.snake_bites[0].forward(SNAKE_STEP)
    
    def turn(self,angle):
        self.snake_bites[0].right(angle)
    
    def grow(self):
        new_bite = turtle.Turtle("square")
        new_bite.color("white")
        new_bite.penup()
        new_x = self.snake_bites[-1].xcor()
        new_y = self.snake_bites[-1].ycor()
        new_bite.goto((new_x,new_y))
        self.snake_bites.append(new_bite)
    
    def head(self):
        return self.snake_bites[0]

    def up(self):
        current_heading = self.head().heading()
        if current_heading == 270:
            return
        self.snake_bites[0].setheading(90)
    def down(self):
        current_heading = self.head().heading()
        if current_heading == 90:
            return
        self.snake_bites[0].setheading(270)
    def right(self):
        current_heading = self.head().heading()
        if current_heading == 180:
            return
        self.snake_bites[0].setheading(0)
    def left(self):
        current_heading = self.head().heading()
        if current_heading == 0:
            return
        self.snake_bites[0].setheading(180)

