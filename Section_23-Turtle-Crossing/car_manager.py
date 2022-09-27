from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.car_list = []
        self.move_speed = 0.1

    def spawn_car(self):
        spawn_chance = random.randint(1, 6)
        if spawn_chance == 1:
            self.car_creation()

    def car_creation(self):
        random_y = random.randint(-240, 270)
        new_car = Turtle("square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.color(random.choice(COLORS))
        new_car.penup()
        new_car.setheading(180)
        new_car.goto(x=300, y=random_y)
        self.car_list.append(new_car)

    def move(self):
        for car in self.car_list:
            car.forward(MOVE_INCREMENT)

    def speed_up(self):
        self.move_speed *= .8
