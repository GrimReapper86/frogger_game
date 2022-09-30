from turtle import Turtle


class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update_level()

    def update_level(self):
        self.clear()
        self.goto(0, 240)
        self.write(f"Level = {self.level}", align="center", font=("Courier", 20, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", move=False, align="center", font=("Courier", 20, "normal"))

    def next_level(self):
        self.level += 1
        self.update_level()
