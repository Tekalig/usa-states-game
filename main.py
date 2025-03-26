from turtle import Turtle, Screen
import pandas as pd

# set up the screen image of the USA State
screen = Screen()
screen.title("U.S State Game")
image = "./assets/blank_states_img.gif"
screen.addshape(image)
Turtle().shape(image)

# reading csv file using pandas
df = pd.read_csv("./data/50_states.csv", index_col=0)

# create the State name writer
turtle = Turtle(visible=False)
turtle.hideturtle()
turtle.penup()


# return location of the states
def location(stateName):
    return int(df.loc[stateName]["x"]), int(df.loc[stateName]["y"])


num_states = 0
play_game = True
guessed_state = []

while play_game:
    state_name = screen.textinput(f"{num_states}/{len(df)} State Name", "Enter U.S State Name:").title()
    if state_name in df.index:
        guessed_state.append(state_name)
        turtle.goto(location(state_name))
        turtle.write(f"{state_name}", align="center")

    if state_name.lower() == "exit":
        play_game = False
        missed_state = [state for state in df.index if state not in guessed_state]
        missed_state = pd.DataFrame(missed_state, columns=["State"])
        missed_state.to_csv("./data/state to learn.csv")

    num_states += 1

screen.exitonclick()
