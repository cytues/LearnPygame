#-*- coding:utf-8 -*-
import pygame
from pygame.locals import *
from sys import exit

from random import *
from math import pi

pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)
points = []

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        #按任意键清屏
        if event.type == KEYDOWN:
            points = []
            screen.fill((255, 255, 255))
        #如果鼠标被按下
        if event.type == MOUSEBUTTONDOWN:
            screen.fill((255, 255, 255))
            #画随机矩形
            rc = (randint(0, 255), randint(0, 255), randint(0, 255))#随机颜色
            rp = (randint(0, 639), randint(0, 479))#随机左上坐标
            rs = (639 - randint(rp[0], 639), 479-randint(rp[1], 479))#随机右下坐标
            pygame.draw.rect(screen, rc, Rect(rp, rs))
            #画随机圆
            rc = (randint(0, 255), randint(0, 255), randint(0, 255))#随机颜色
            rp = (randint(0, 639), randint(0, 479))#随机圆心
            rr = randint(1, 200)#随机半径
            pygame.draw.circle(screen, rc, rp, rr)
            #得到鼠标的位置
            x, y = pygame.mouse.get_pos()
            #添加点
            points.append((x, y))
            #角度随鼠标移动改变
            angle = (x/639.)*pi*2
            #根据点击位置画弧线
            pygame.draw.arc(screen, (0, 0, 0), (0, 0, 639, 479), 0, angle, 3)
            #根据点击位置画椭圆
            pygame.draw.ellipse(screen, (0, 255, 0), (0, 0, x, y))
            #从左上和右下画两根线连接到点击位置
            pygame.draw.line(screen, (0, 0, 255), (0, 0), (x, y))
            pygame.draw.line(screen, (255, 0, 0), (640, 480), (x, y))
            #画点击轨迹图
            if len(points) > 1:
                pygame.draw.lines(screen, (155, 155, 0), False, points, 2)
            #将点画成小圆（更明显）
            for p in points:
                pygame.draw.circle(screen, (155, 155, 155), p, 3)
    #刷新
    pygame.display.update()
