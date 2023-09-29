import turtle
from turtle import Turtle
class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.movespeed=0.1
        self.speed(1)
        self.xmove = 10
        self.ymove = 10

    def bounce_y(self):
        self.ymove *= -1

    def bounce_x(self):
        self.xmove *= -1
        self.movespeed *= 0.9

    def move(self):
        self.penup()
        self.goto(self.xcor()+self.xmove, self.ycor()+self.ymove)

    def reset_position(self):
        self.goto(0, 0)
        self.movespeed = 0.1
        self.bounce_x()