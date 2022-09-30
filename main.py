from turtle import Screen
from Frog import Frog
from Cars import Car
from Level import Level
from Lane_draw import Lane
import time

Lane = Lane()
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Frog GAME")
screen.tracer(0)
all_cars = []

frog = Frog((0, -270))
for i in range(9):
    car = Car()
    all_cars.append(car)
level = Level()
screen.listen()
screen.onkey(fun=frog.up, key="Up")
screen.onkey(fun=frog.down, key="Down")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(car.move_speed)
    for i in range(9):
        all_cars[i].move()
screen.exitonclick()
