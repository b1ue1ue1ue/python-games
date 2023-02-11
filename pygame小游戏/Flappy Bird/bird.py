import pygame
from random import *
from time import sleep
pygame.init()

map_width=284
map_height=512
frame=1
FPS=60
pipes=[[200,4]]
gravity=0.1
velocity=0

#pygame的游戏框 pygame.display.set_mode函数
gameScreen=pygame.display.set_mode((map_width,map_height))
#pygame的时间函数
clock=pygame.time.Clock()
#背景
background=pygame.image.load("images/background.png")
#小鸟翅膀向上
bird_wing_up=bird_wing_up_copy=pygame.image.load("images/bird_wing_up.png")
#小鸟翅膀向上
bird_wing_down=bird_wing_down_copy=pygame.image.load("images/bird_wing_down.png")
#管道身子
pipe_body=pygame.image.load("images/pipe_body.png")
#管道末尾
pipe_end=pygame.image.load("images/pipe_end.png")
#鸟的坐标
bird=[20,map_height//2]

def reset():
    global frame,pipes,bird,gravity,velocity
    frame=1
    bird=[20,map_height//2]
    pipes.clear()
    pipes=[[200,4]]
    gravity=0.1
    velocity=0

def draw_bird(x,y):
    global frame
    if frame>=1 and frame<=30:
        gameScreen.blit(bird_wing_up,(x,y))
        frame+=1
    elif frame>30 and frame<=60:
        gameScreen.blit(bird_wing_down,(x,y))
        frame+=1
        if frame==61:
            frame=1
def draw_pipes():
    global pipes
    for i in range(len(pipes)):
        for m in range(pipes[i][1]):
            gameScreen.blit(pipe_body,(pipes[i][0],m*32))
        for m in range(pipes[i][1]+6,16):
            gameScreen.blit(pipe_body,(pipes[i][0],m*32))
        gameScreen.blit(pipe_end,(pipes[i][0],pipes[i][1]*32))
        gameScreen.blit(pipe_end,(pipes[i][0],(pipes[i][1]+5)*32))
        pipes[i][0]-=1
def hit():
    if bird[1]>map_height-35:
        print("hit floor")
        return False
    if bird[1]<0:
        print("hit ceiling")
        return False
    if pipes[0][0]-30<bird[0]<pipes[0][0]+79:
        if bird[1]<(pipes[0][1]+1)*32 or bird[1]>(pipes[0][1]+4)*32:
            print("hit pipe")
            return False
    return True

def gameLoop():
    global bird,velocity,gravity,bird_wing_down,bird_wing_up
    while True:
        if len(pipes)<4:
            x=pipes[-1][0]+200
            open_pos=randrange(1,10)
            pipes.append([x,open_pos])
        if pipes[0][0]<-80:
            pipes.pop(0)
        #gamescreen这里显示图片background在0,0位置
        safe=hit()
        bird[1]+=velocity
        velocity+=gravity
        bird_wing_down=pygame.transform.rotate(bird_wing_down_copy,
                                               -90*(velocity/15))
        bird_wing_up=pygame.transform.rotate(bird_wing_up_copy,
                                               -90*(velocity/15))
        gameScreen.blit(background,(0,0))
        draw_bird(bird[0],bird[1])
        draw_pipes()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN:
                bird[1]-=40
                velocity=0
            if event.type==pygame.QUIT:
                pygame.quit()
                return
        if not safe:
            sleep(3)
            reset()
        clock.tick(FPS) #每秒刷新60次

        bird[1]=min(bird[1],512-32)
        bird[1]=max(bird[1],0)


gameLoop()