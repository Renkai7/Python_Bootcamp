from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def counter_clockwise():
    tim.right(10)
    move_forward()


def clockwise():
    tim.left(10)
    move_forward()

def clear_screen():
    tim.clear()
    tim.reset()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()

# Notes
# Higher Order Function: function that works within a function
# Use position arguments instead of key arguments for functions inside another function
