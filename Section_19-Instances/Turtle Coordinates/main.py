import turtle
from turtle import Turtle, Screen
import random

# Screen setup
screen = Screen()
screen.setup(width=500, height=400)

# User bet input
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

# Color list for turtles
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# Turtle list
all_turtles = []

is_race_on = False
y_cor = -100

for i in range(len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_cor)
    all_turtles.append(new_turtle)
    y_cor += 30

# Only start race when user makes a bet
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
