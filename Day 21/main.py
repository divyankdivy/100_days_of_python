from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


sc = Screen()
sc.setup(600, 600)
sc.bgcolor("black")
sc.title("My Snake Game")
sc.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

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

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        scoreboard.game_over()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            scoreboard.game_over()

sc.exitonclick()