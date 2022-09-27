import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Setup Screen
screen = Screen()
screen.setup(width=600, height=600)

# Turn off animation
screen.tracer(0)

# Setup Scoreboard
scoreboard = Scoreboard()

# Create Turtle player
player = Player()

# Create Cars
cars = CarManager()

# Player movement - Keypress
screen.listen()
screen.onkey(key="w", fun=player.move_up)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(cars.move_speed)
    cars.spawn_car()
    cars.move()

    for car in cars.car_list:
        if player.distance(car) < 15:
            game_is_on = False
            scoreboard.game_over()
    if player.reach_finish_line():
        scoreboard.increase_level()
        cars.speed_up()

screen.exitonclick()

