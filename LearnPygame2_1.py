#-*- coding:utf-8 -*-
background_image_filename = "./images/sushiplate.jpg"

import pygame
from pygame.locals import *
from sys import exit
#初始化
pygame.init()
#设置窗口
screen = pygame.display.set_mode((640, 480), 0, 32)
background = pygame.image.load(background_image_filename).convert()
#初始点设置为左上角
x, y = 0, 0
move_x, move_y = 0, 0
#循环进行
while True:
    #for循环捕捉每次出现的事件
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        #如果键盘被按下
        if event.type == KEYDOWN:
            #按下左键x左边减1，左移
            if event.key == K_LEFT:
                move_x = -1
            elif event.key == K_RIGHT:
                move_x = 1
            elif event.key == K_UP:
                move_y = -1
            elif event.key == K_DOWN:
                move_y = 1
        #如果放开键盘，图不动
        elif event.type == KEYUP:
            move_x = 0
            move_y = 0
    #计算新的x，y坐标
    x += move_x
    y += move_y

    screen.fill((0, 0, 0))
    screen.blit(background, (x, y))
    #刷新
    pygame.display.update()

