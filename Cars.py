from turtle import Turtle
import random

COLOR = ['yellow', 'blue', 'white', 'orange', 'red']
LOCATIONS = [-225, -175, -125, -75, -25, 25, 75, 125, 225]
DIRECTION = [-1, 1]


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.color(random.choice(COLOR))
        self.shape('square')
        self.penup()
        self.seth(90)
        self.shapesize(stretch_wid=random.randint(3, 6), stretch_len=1)
        self.direction = random.choice(DIRECTION)
        self.goto(self.direction * 350, self.direction * random.choice(LOCATIONS))
        self.x_move = self.direction * -10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        self.goto(new_x, self.ycor())
