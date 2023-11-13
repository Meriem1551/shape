from turtle import *

drawing_area = Screen()
drawing_area.bgcolor("black")
drawing_area.setup(width=1440, height=780, startx=0, starty=0)
flower = Turtle()
flower.speed(20)
colors = [
    "#BF3EFF",
    "#BF3EFF",
    "#BF3EFF",
    "#B23AEE",
    "#B23AEE",
    "#B23AEE",
    "#9A32CD",
    "#9A32CD",
    "#9A32CD",
    "#68228B",
    "#68228B",
    "#68228B",
    "#68228B",
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
