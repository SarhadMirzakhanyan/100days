import turtle
import time
from paddle import Paddle
from ball import Ball
from screen import Screen

left_points = 0
right_points = 0

screen_obj = Screen()
screen = screen_obj.get_screen()

paddle_left = Paddle("left",screen.screensize())
screen.onkey(paddle_left.move_up,"w")
screen.onkey(paddle_left.move_down,"s")
paddle_right = Paddle("right",screen.screensize())
screen.onkey(paddle_right.move_up,"Up")
screen.onkey(paddle_right.move_down,"Down")

score_left = turtle.Turtle(shape="blank",visible=False)
score_left.color("white")
score_left.penup()
score_left.goto(50,250)


score_right = turtle.Turtle(shape="blank",visible=False)
score_right.color("white")
score_right.penup()
score_right.goto(-50,250)


ball = Ball()
game_is_on = True
screen_width_border = screen.window_width()/2 - 20
while game_is_on:

    time.sleep(0.1)

    ball.move()
    if ball.xcor() > screen_width_border:
        left_points += 1
        ball.goto(0,0)
        score_left.clear()
        ball.bounce_x()
        time.sleep(1)
    
    if ball.xcor() < -screen_width_border:
        right_points += 1 
        ball.goto(0,0)
        score_right.clear()
        ball.bounce_x()
        time.sleep(1)

    if ball.hit_paddle(paddle_obj=paddle_left) or ball.hit_paddle(paddle_obj=paddle_right):
        ball.bounce_x()
    score_right.write(right_points,font=("",24,""))
    score_left.write(left_points,font=("",24,""))
    screen.update()


screen.update()
screen.exitonclick()