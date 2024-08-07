from turtle import Screen
from player import Player
from car import Car
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("white")
screen.tracer(0)
screen.title("Turtle Crossing")

score = ScoreBoard()
game_on = True
player = Player()
screen.listen()
screen.onkeypress(key="Up", fun=player.go_forward)
counter = 0
cars = []
no_of_cars = 0
while game_on:
    counter += 1
    time.sleep(0.1)
    screen.update()
    if(counter%6 == 0):
        car = Car()
        cars.append(car)
        no_of_cars += 1
    for i in cars:
        i.go_forward()

    #detect collision
    for i in cars:
        if player.distance(i) < 50 and player.ycor()>i.ycor()-30:
            score.game_over()
            game_on = False

    if player.ycor() >=280:
        score.increase_point()
        for i in cars:
            i.speed_up()
        player.reset()



screen.exitonclick()