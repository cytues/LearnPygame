#-*- coding:utf-8 -*-
import pygame
from pygame.locals import *
from sys import exit

pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)

font = pygame.font.Font("./font/simsun.ttc", 40)

text_surface = font.render(u"你好", True, (0, 0, 255))
#定义字体的起始位置
x = 0
y = (480 - text_surface.get_height()) / 2
#背景图
background = pygame.image.load("./images/sushiplate.jpg").convert()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.blit(background, (0, 0))
    #字体不断的向左移动2个像素，太快可以改小数值
    x -= 2
    #如果字体超出窗口宽度，则从头开始
    if x < -text_surface.get_width():
        x = 640 - text_surface.get_width()
    #建立字体页面
    screen.blit(text_surface, (x, y))
    #刷新
    pygame.display.update()
