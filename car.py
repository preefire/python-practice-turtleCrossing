from turtle import Turtle
import random as r
COLOURS = ["red", "green", "orange", "pink", "green", "yellow"]
SPEED = 10
class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.generate_car()
        self.speed = SPEED

    def generate_car(self):
        self.penup()
        self.setheading(180)
        self.shape("square")
        self.shapesize(2,4)
        self.color(r.choice(COLOURS))
        self.goto(300,r.randint(-240,240))
        #self.goto(300, r.randint(0,0))

    def go_forward(self):
        self.fd(SPEED)

    def speed_up(self):
        self.speed = 10*self.speed


