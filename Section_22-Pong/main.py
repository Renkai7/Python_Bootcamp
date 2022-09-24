import time
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

# Positioning for right and left paddles
RIGHT_POS = (350, 0)
LEFT_POS = (-350, 0)

# Setup screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")

# Setup Scoreboard
scoreboard = Scoreboard()

# Turn off animation
screen.tracer(0)

# Create paddles
r_paddle = Paddle(RIGHT_POS)
l_paddle = Paddle(LEFT_POS)

# Key press for user
screen.listen()
screen.onkeypress(key="w", fun=r_paddle.move_up)
screen.onkeypress(key="s", fun=r_paddle.move_down)
screen.onkeypress(key="Up", fun=l_paddle.move_up)
screen.onkeypress(key="Down", fun=l_paddle.move_down)

# Setup ball
ball = Ball()


# Gameplay
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detect ball collision with ceiling or floor
    if ball.ycor() > 280 or ball.ycor() < -280 or ball.xcor() > 400 or ball.xcor() < -400:
        ball.bounce_y()

    # Detect ball collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect right paddle misses ball
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
        print("Point for left paddle!")

    elif ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
        print("Point for right paddle!")


screen.exitonclick()
