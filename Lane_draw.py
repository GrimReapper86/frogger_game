from turtle import Turtle


class Lane(Turtle):
    """Draws 10 lanes """
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        for i in range(9):
            self.goto(-400, -250 + 50 * i)
            self.pendown()
            self.goto(400, -250 + 50 * i)
            self.penup()
