import turtle
import random

screen = turtle.Screen()
screen.setup(width=600,height=500)
colors = ["red","orange","yellow","green","blue","cyan","purple"]
starting_y_coordinate = -180
turtles_list = []
race_on = True

arno_bet = screen.textinput("Winner","Arno, Place a bet on one of the turtles")
tigran_choice = screen.textinput("Winner","Tigran, Place a bet on one of the turtles")

for turtle_index in range(0,7):
    new_turtle = turtle.Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x = -240, y=starting_y_coordinate + 60*turtle_index)
    turtles_list.append(new_turtle)

while race_on:
    for t in turtles_list:
        t.forward(random.randint(1,10))
        if t.xcor() >= 280:
            print("End of competition")
            winning_turtle = t.pencolor()
            print(f"Winning turtle is: {winning_turtle}")
            if arno_bet == winning_turtle:
                print("Arno won!")
            elif tigran_choice == winning_turtle:
                print("Tigran won")
            else:
                print("You lost...")
            race_on = False
            break


screen.exitonclick()
