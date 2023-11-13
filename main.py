from turtle import *

drawing_area = Screen()
drawing_area.bgcolor("black")
drawing_area.setup(width=1440, height=780, startx=0, starty=0)
flower = Turtle()
flower.speed(20)
colors = [
    "#b88f96",
    "#c29fa5",
    "#ccaeb3",
    "#d6bec2",
    "#dac4c8",
    "#decbce",
    "#e2d1d4",
    "#e6d8da",
    "#eadee0",
    "#eee5e6",
    "#f2ebec",
    "#f6f2f2",
    "#faf8f8",
    "#ffffff",
]

for i in range(13):
    flower.color(colors[i])
    for j in range(40):
        flower.forward(150)
        flower.right(130)
    flower.penup()
    flower.forward(350)
    flower.left(50)
    flower.pendown()

drawing_area.exitonclick()
