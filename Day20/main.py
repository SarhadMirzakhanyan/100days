import turtle
import time
import snake
import food
import scoreboard

screen = turtle.Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)
snaky =  snake.Snake()

screen.listen()
screen.onkey(snaky.up,"Up")
screen.onkey(snaky.down,"Down")
screen.onkey(snaky.left,"Left")
screen.onkey(snaky.right,"Right")


apple = food.Food([screen.window_width(),screen.window_height()])
score = scoreboard.Scoreboard(screen.window_height())



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    score.show_score()
    snaky.move()
    screen.update()

    if snaky.head().distance(apple) < 14:
       apple.recreate()
       score.add_to_score()
       snaky.grow()
       # print(score)

    if snaky.head().xcor() < -280 or snaky.head().xcor() > 280 or snaky.head().ycor() > 280 or snaky.head().ycor() <-280:
        game_is_on = False
        score.game_over()
    
    for bites in snaky.snake_bites[1:]:
        if snaky.head().distance(bites) < 10:
            game_is_on = False
            score.game_over()
    screen.update()

screen.exitonclick()