import turtle
import pandas as pd
from pprint import pprint

image = "blank_states_img.gif"
screen = turtle.Screen()
screen.title("US states game")
screen.addshape(name=image)
turtle.shape(image)

states_file = pd.read_csv("50_states.csv")
states = states_file['state'].to_list()
guessed_states = []
loop_condition = True

while loop_condition:
    input_state = screen.textinput("State name", "Type a state name:")
    input_state = input_state.title()
    if input_state in states:
        print(f"State {input_state} exists")
        state_series = states_file[states_file['state'] == input_state]
        state_coord = list(zip(state_series.x, state_series.y))
        state_text = turtle.Turtle(visible=False)
        state_text.penup()
        state_text.goto(state_coord[0])
        state_text.write(input_state, move=False, align="center")
        guessed_states.append(input_state)
        states.pop(states.index(input_state))
    elif input_state is None:
        print('Exiting the game...')
        loop_condition = False
    elif input_state in guessed_states:
        print(f"You've already guessed {input_state}")
    else:
        print(f"State {input_state} doesn't exist")
    if len(guessed_states) >= 50:
        loop_condition = False
        print("You guessed all the states, good job")

