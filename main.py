import turtle
from turtle import Turtle, Screen
import pandas as pd

screen = Screen()
screen.title("U.S State game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()
print(all_states)
guessed_state = []
state = 0
while len(guessed_state) < 50:
    answer_state = screen.textinput(title= f"Guess the state: {state}/50", prompt= "What's another state").title()

    if answer_state == "Exit":
        missing_state = []
        for state in all_states:
            if state not in guessed_state:
                missing_state.append(state)
        new_data = pd.DataFrame(missing_state)
        new_data.to_csv("states to learn.csv")
        break
    if answer_state in all_states:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
        t.write(answer_state)
        state += 1



