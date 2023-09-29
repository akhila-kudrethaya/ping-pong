from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.lscore = 0
        self.rscore = 0
        self.updatescore()

    def updatescore(self):
        self.clear()
        self.goto(-100,240)
        self.write(self.lscore,align = "center", font = ("courier", 40, "normal"))
        self.goto(100, 240)
        self.write(self.rscore, align="center", font=("courier", 40, "normal"))

    def lpoint(self):
        self.lscore += 1
        self.updatescore()

    def rpoint(self):
        self.rscore += 1
        self.updatescore()