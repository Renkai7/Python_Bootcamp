from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.goto(-280, 265)
        self.level = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        self.clear()
        self.level += 1
        self.update_scoreboard()
        print(self.level)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", font=FONT)
