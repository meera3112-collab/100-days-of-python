import random
import turtle
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

turtle.colormode(255)

tim.setheading(225)
tim.penup()
tim.forward(300)
tim.setheading(0)

color_list = [
    (244, 240, 231), (223, 232, 241), (245, 231, 238), (231, 243, 236),
    (204, 159, 107), (231, 213, 109), (134, 168, 192), (44, 105, 144),
    (152, 78, 53), (199, 142, 164), (15, 32, 53), (181, 159, 42),
    (148, 65, 87), (141, 178, 155), (205, 91, 70), (64, 117, 92),
    (195, 89, 118), (225, 170, 187), (15, 38, 27), (59, 34, 19),
    (227, 175, 166), (48, 158, 182), (238, 213, 4), (87, 155, 112),
    (121, 35, 53), (177, 188, 216), (35, 58, 110), (169, 206, 184),
    (60, 21, 36), (14, 96, 71)
]

number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen.exitonclick()
