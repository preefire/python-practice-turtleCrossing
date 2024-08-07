from turtle import Turtle
FD_DIST = 10
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.setheading(90)
        self.goto(0,-280)

    def go_forward(self):
        self.fd(FD_DIST)

    def reset(self):
        self.goto(0,-280)
