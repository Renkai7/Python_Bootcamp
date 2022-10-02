import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
data = pandas.read_csv("50_states.csv")
screen.addshape(image)

turtle.shape(image)

state = turtle.Turtle()
state.hideturtle()
state.speed(0)
state.penup()

state_list = data.state.to_list()
guessed_states = []
missed_states = []

while len(guessed_states) < 50:

    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()

    if answer_state == "Exit":
        break
    if answer_state in state_list:
        state_data = data[data.state == answer_state]
        state.goto(x=int(state_data.x), y=int(state_data.y))
        state.write(answer_state)
        if answer_state not in guessed_states:
            guessed_states.append(answer_state)

    if len(guessed_states) == 50:
        state.goto(0, 300)
        state.write(f"{len(guessed_states)}/50 States Correct! You have guessed all the states!",
                    font=('arial', 20, "bold"), align="center")

for state in state_list:
    if state not in guessed_states:
        missed_states.append(state)

my_data = pandas.DataFrame(missed_states)
my_data.to_csv("states_to_learn.csv")
