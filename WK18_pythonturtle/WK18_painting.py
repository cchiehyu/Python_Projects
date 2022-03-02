# import colorgram
#
# rgb_colors = []
# # Extract 6 colors from an image.
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
import random
import turtle as turtle_module
turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.hideturtle()
tim.penup()
color_list = [(58, 106, 148), (224, 200, 110), (134, 85, 59), (222, 139, 64), (195, 145, 171), (144, 179, 202), (139, 81, 104), (209, 91, 69), (68, 106, 90)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots =100

for dot_count in range(1,number_of_dots+1):
    tim.dot(20,random.choice(color_list))
    tim.forward(50)

    if dot_count %10 ==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()


