from turtle import Turtle, Screen
from snake import Snake
import time


sc = Screen()
sc.setup(600, 600)
sc.bgcolor("black")
sc.title("My Snake Game")
sc.tracer(0)

snake = Snake()

sc.listen()
sc.onkey(snake.up, "Up")
sc.onkey(snake.down, "Down")
sc.onkey(snake.right, "Right")
sc.onkey(snake.left, "Left")

game_on = True
while game_on:
    sc.update()
    time.sleep(0.1)
    snake.move()

sc.exitonclick()
