import turtle
from turtle import*

def circle(x,y,size,color_name):
    up()
    goto(x,y)
    dot(size,color_name)

def square(x,y,size,color_name):
    up()
    goto(x,y)
    down()
    color(color_name)
    begin_fill()
    forward(size)
    left(90)
    forward(size)
    left(90)
    forward(size)
    left(180)
    end_fill()

def line(x,y,a,b,line_width=20,color_name="black"):
    up()
    goto(x,y)
    down()
    color(color_name)
    width(line_width)
    goto(a,b)
