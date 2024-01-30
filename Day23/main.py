import turtle


screen = turtle.Screen()
screen.tracer(0)
turtle_position = (0, -abs(screen.screensize()[1]))
loop_condition = True
my_turtle = turtle.Turtle(shape="turtle")
my_turtle.penup()
my_turtle.seth(90)
my_turtle.setpos(turtle_position)
screen.update()
screen.exitonclick()

#while loop_condition:
