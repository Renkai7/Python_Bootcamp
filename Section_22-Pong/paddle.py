from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, pos):
        super(Paddle, self).__init__()

        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.color("white")
        self.penup()
        self.goto(x=pos[0], y=pos[1])
        self.setheading(90)

    def move_up(self):
        self.forward(10)

    def move_down(self):
        self.backward(10)
