import turtle as t
from turtle import Screen
import random

tim = t.Turtle()
t.colormode(255)
tim.shape("turtle")


# RANDOM COLOR
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


# DRAW SQUARE
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

# DOTTED LINE
# for _ in range(10):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# DRAW SHAPES
# colors = ["red", "blue", "green", "purple", "orange", "coral", "pink"]
# sides = 3
# for _ in range(7):
#     angle = 360 / sides
#     tim.color(random.choice(colors))
#     for _ in range(sides):
#         tim.forward(100)
#         tim.right(angle)
#     sides += 1

# RANDOM WALK
# directions = [0, 90, 180, 270]
# tim.pensize(10)
# tim.speed(0)
# for _ in range(100):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.right(random.choice(directions))

# DRAW SPIROGRAPH
tim.speed(0)
def draw_circle(gap_size):
    for _ in range(int(360 / gap_size)):
        tim.color(random_color())
        tim.setheading(tim.heading() + gap_size)
        tim.circle(100)

draw_circle(5)




screen = Screen()
screen.exitonclick()
