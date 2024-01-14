import turtle

tim = turtle.Turtle()
screen = turtle.Screen()



def forward():
    tim.forward(5)

def backward():
    tim.backward(5)
    #tim.forward(5)

def counter_clockwise():
    tim.left(3)
    tim.forward(5)
    #tim.forward(5)

def clockwise():
    tim.right(3)
    tim.forward(5)
    #tim.forward(5)
def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(fun=forward,key="w")
screen.onkey(fun=backward,key="s")
screen.onkey(fun=counter_clockwise,key="a")
screen.onkey(fun=clockwise, key="d")
screen.onkey(fun=clear_screen,key="c")
screen.exitonclick()