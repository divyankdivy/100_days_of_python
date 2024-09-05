from turtle import Turtle, Screen
import random

is_race_on = False

screen = Screen()
screen.setup(500,400)
user_bet = screen.textinput("Make your bet: ","Which turtle will win the race? Enter the color: ")
color = ["orange", "red", "green", "blue", "purple", "yellow"]
y_position = [-70, -40, -10, 20, 50, 80]

all_turtle = []

for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color[i])
    new_turtle.penup()
    new_turtle.goto(-230, y_position[i])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_col = turtle.pencolor()
            if winning_col == user_bet:
                print(f"You've won! The {winning_col} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_col} turtle is the winner!")
        move = random.randint(1, 5)
        turtle.forward(move)


screen.exitonclick()