import turtle
from random import choice
from turtle import*
from gamebase import circle,line
plate_pos=0
plate_length=250
plate_width=20
plate_speed=50
apple_x=0
apple_y=0
apple_color="red"
apple_speed=5
size=20
apple_speedx=choice([-apple_speed,apple_speed])
apple_speedy=choice([-apple_speed,apple_speed])
def draw():
    clear()
    circle(apple_x, apple_y, size, "red")
    line(plate_pos-plate_length/2,-230,plate_pos+plate_length/2,-230,plate_width,"black")
    update()
def turnleft():
    global  plate_pos
    plate_pos-=plate_speed
    draw()

def turnright():
    global plate_pos
    plate_pos+=plate_speed
    draw()
def hit():
    if apple_x<plate_pos-plate_length/2 or apple_x>plate_pos+plate_length/2:
        return True
    else:
        return False
def gameLoop():
    global apple_x,apple_y
    draw()
    global apple_speedx,apple_speedy
    if apple_x-size/2==-500:
        apple_speedx=-apple_speedx
    if apple_x+size/2==500:
        apple_speedx=-apple_speedx
    if apple_y+size/2==250:
        apple_speedy=-apple_speedy
    if apple_y-size/2==-230+plate_width/2:
        if hit():
            return
        apple_speedy=-apple_speedy
    apple_x += apple_speedx
    apple_y += apple_speedy
    ontimer(gameLoop,t=10)

setup(1000,500,0,0)
hideturtle()
tracer(False)
listen(10)
onkey(lambda:turnleft(),"a")
onkey(lambda:turnright(),"d")
gameLoop()
done()
