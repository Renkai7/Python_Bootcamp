from turtle import Turtle

# Constants
MOVE_DISTANCE = 20
MOVE_UP = 90
MOVE_RIGHT = 0
MOVE_DOWN = 270
MOVE_LEFT = 180


class Snake:
    def __init__(self):
        self.segments = []
        self.x_cor = 0
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for _ in range(3):
            self.add_segment()

    # Makes snake longer
    def add_segment(self):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(x=self.x_cor, y=0)
        self.segments.append(new_segment)
        self.x_cor -= 20

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != MOVE_DOWN:
            self.head.setheading(MOVE_UP)

    def right(self):
        if self.head.heading() != MOVE_LEFT:
            self.head.setheading(MOVE_RIGHT)

    def down(self):
        if self.head.heading() != MOVE_UP:
            self.head.setheading(MOVE_DOWN)

    def left(self):
        if self.head.heading() != MOVE_RIGHT:
            self.head.setheading(MOVE_LEFT)
