import turtle
import time
from paddle import Paddle
from ball import Ball
from screen import Screen
from scoreboard import Scoreboard

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

score = Scoreboard()


ball = Ball()
game_is_on = True
screen_width_border = screen.window_width()/2 - 20

while game_is_on:
    time.sleep(ball.speed)

    ball.move()
    if ball.xcor() > screen_width_border:
        ball.goto(0,0)
        score.point_left()
        ball.bounce_x()
        ball.speed = 0.1
        time.sleep(1)
    
    if ball.xcor() < -screen_width_border:
        ball.goto(0,0)
        score.point_right()
        ball.bounce_x()
        ball.speed = 0.1
        time.sleep(1)

    if ball.hit_paddle(paddle_obj=paddle_left) or ball.hit_paddle(paddle_obj=paddle_right):
        ball.bounce_x()
    screen.update()

screen.update()
screen.exitonclick()