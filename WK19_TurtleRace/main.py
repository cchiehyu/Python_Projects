import turtle
from turtle import Turtle, Screen
import random
screen = Screen()
#
# def move_forwards():
#     tim.forward(10)
# def move_backwards():
#     tim.backward(10)
# def turn_left():
#     new_heading = tim.heading()+10
#     tim.setheading(new_heading)
# def turn_right():
#     new_heading = tim.heading()-10
#     tim.setheading(new_heading)
# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
# screen.listen()
# screen.onkey(move_forwards,"w") #fun=function that is going to use
# screen.onkey(move_backwards,"s")
# screen.onkey(turn_left,"a")
# screen.onkey(turn_right,"d")
# screen.onkey(clear,"c")

is_race_on = False
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt ="Which turtle will win the race?(Rainbow color): ")
print(user_bet)
colors =["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:   #each turtle is 40*40
            is_race_on = False
            winner_color = turtle.pencolor()
            if winner_color == user_bet:
                print(f"YOU WON! {winner_color} turtle win")
            else:
                print(f"YOU LOSE! {winner_color} turtle is the real winner")

        random_distance = random.randint(0,10)
        turtle.forward(random_distance)








screen.exitonclick()
