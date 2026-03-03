import turtle
from turtle import Turtle, Screen
import random
is_race_on = False
screen = Screen()
screen.setup(width=500, height= 400)

user_bet = screen.textinput(title="Make a Bet", prompt="Which color turtle will win the race?: ")
colors = ["red", "blue", "green", "yellow", "purple", "cyan", "pink", "black"]

y_postion = [-100,-70, -40, -10, 20, 50, 80, 110]

all_turtles = []
for turtle_index in range(0,8):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_postion[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        #print(turtle)
        rand_distance = random.randint(0,10)
        if turtle.color() == colors[7]:
            rand_distance = rand_distance * 1.15

        turtle.forward(rand_distance)

        if turtle.xcor() > 230:
            print(turtle.pencolor())
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You Win! The {winning_color} turtle is the winner!")
            else:
                print(f"You lost! The {winning_color} turtle is the winner!")
            is_race_on = False


screen.exitonclick()