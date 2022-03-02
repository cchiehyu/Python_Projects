# import turtle
# from turtle import Turtle, Screen
# import random
#
# tur = Turtle()
# tur.shape("turtle")
# # tur.color("pink")

#draw a square
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# for _ in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.left(90)

#draw dash line
# for _ in range(10):
#     tur.forward(2)
#     tur.penup()
#     tur.forward(2)
#     tur.pendown()

# draw any polygon in turtle
#input the size of the polygon

# draw any polygon in turtle + change the color of each line
# colours = ["navy","teal", "orange","dark olive green","indian red","dark slate blue","floral white","pink"]
#
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tur.forward(100)
#         tur.right(angle)
# for shape_side_n in range(3,11):
#     tur.color(random.choice(colours))
#     draw_shape(shape_side_n)


# colours = ["navy","teal", "orange","dark olive green","indian red","dark slate blue","pink","red"]
# directions = [0,90,180,270] #東西南北
# tur.pensize(15)
# tur.speed("fastest")
# for _ in range(100):
#     tur.color(random.choice(colours))
#     tur.forward(30)
#     tur.setheading(random.choice(directions))


#draw muti circles in different colors
import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

tim.speed("fastest")

def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading()+size_of_gap)

draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()