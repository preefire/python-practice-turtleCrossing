from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.ht()
        self.goto(x=0, y=260)
        self.color("black")
        self.write(f"Score = {self.score}", align="center", font=("Arial", 15, "bold"))

    def increase_point(self):
        self.score += 1
        self.clear()
        self.write(f"Score = {self.score}", align="center",font=("Arial",15,"bold"))


    def game_over(self):
        self.goto(x=0, y=-230)
        self.write("Game Over", align="center", font=("Arial", 35, "bold"))
