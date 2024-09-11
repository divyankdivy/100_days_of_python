from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((370, 0))
l_paddle = Paddle((-370, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")



game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect Collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with right paddle
    if (ball.xcor() > 340 and ball.distance(r_paddle) < 50) or (ball.xcor() < -340 and ball.distance(l_paddle) < 50):
        ball.bounce_x()

    if ball.xcor() > 390:
        ball.reset_position()
        ball.bounce_x()
        scoreboard.l_point()

    if ball.xcor() < -390:
        ball.reset_position()
        ball.bounce_x()
        scoreboard.r_point()

screen.exitonclick()
