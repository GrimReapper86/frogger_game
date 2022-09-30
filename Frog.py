from turtle import Turtle


class Frog(Turtle):
    """ Draw a Frog that is been controlled by up and down arrow """
    def __init__(self, position):
        super().__init__()
        self.color('green')
        self.shape('turtle')
        self.penup()
        self.seth(90)
        self.speed("fastest")
        self.goto(position)

    def up(self):
        new_cord = self.ycor() + 20
        self.goto(self.xcor(), new_cord)

    def down(self):
        new_cord = self.ycor() - 20
        self.goto(self.xcor(), new_cord)
