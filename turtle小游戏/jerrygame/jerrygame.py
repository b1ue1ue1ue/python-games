from turtle import *
from gamebase import square
from random import randrange,choice
balloons=[]
size=50
color_option=["red","blue","light blue","pink","dark blue","green","purple"]

def distance(x,y,a,b):
    return ((a-x)**2+(b-y)**2)**0.5
def tap(x,y):
    global balloons
    for n in range(len(balloons)):
        a=balloons[n][0]
        b=balloons[n][1]
        if distance(x,y,a,b)<size/2:
            balloons.pop(n)
            return

def line(x,y,a,b,line_width=1,color_name="black"):
    up()
    goto(x,y)
    down()
    color(color_name)
    width(line_width)
    goto(a,b)


def draw():
    clear()
    for n in range(1,len(balloons)+1):
        line(balloons[-n][0], balloons[-n][1], balloons[-n][0],balloons[-n][1] - size * 1.5, 2)
        up()
        goto(balloons[-n][0],balloons[-n][1])
        dot(size,balloons[-n][2])
        balloons[-n][1]=balloons[-n][1]+2
    update()
def gameLoop():
    if randrange(0,50)==1:
        x=randrange(-210+size/2,210-size/2)
        c=choice(color_option)
        balloons.append([x,-210-size/2,c])
    draw()
    ontimer(gameLoop,t=10)


setup(420,420,0,0)
hideturtle()
tracer(False)
listen()
onscreenclick(tap)
gameLoop()
done()

