from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape('square')
        self.setposition(x, y)
        self.shapesize(5, 1)
        self.color('white')

    def move_up(self):
        self.penup()
        self.goto(self.xcor(),self.ycor()+20)
        
    def move_down(self):
        self.penup()
        self.goto(self.xcor(), self.ycor() - 20)


