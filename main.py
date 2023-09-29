from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from score import ScoreBoard

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor('black')
screen.title('Ping Pong')
screen.tracer(0)
r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
score = ScoreBoard()

y = 325
for _ in range(15):
    y -= 40
    place = (0, y)
    t = Turtle()
    t.shape("square")
    t.shapesize(stretch_wid=1, stretch_len=0.25)
    t.color("white")
    t.penup()
    t.goto(place)

screen.listen()
screen.onkey(key='Up', fun=l_paddle.move_up)
screen.onkey(key='Down', fun=l_paddle.move_down)
screen.onkey(key='1', fun=r_paddle.move_up)
screen.onkey(key='0', fun=r_paddle.move_down)

game_is_on = True
while game_is_on:
    time.sleep(ball.movespeed)
    screen.update()
    ball.move()
    # Detect collision with top wall
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    # Detect collision with paddles
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # Detect if ball moves beyond the side walls
    if ball.xcor() > 380:
        ball.reset_position()
        score.lpoint()

    if ball.xcor() < -380:
        ball.reset_position()
        score.rpoint()

screen.exitonclick()
