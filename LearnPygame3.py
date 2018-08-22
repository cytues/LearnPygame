#-*- coding:utf-8 -*-
background_image_filename = './images/sushiplate.jpg'

import pygame
from pygame.locals import *
from sys import exit

pygame.init()
#默认窗口化
screen = pygame.display.set_mode((640, 480), 0, 32)
background = pygame.image.load(background_image_filename).convert()
#设置flag
Fullscreen = False

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    if event.type == KEYDOWN:
        #如果按下f键则切换到全屏
        if event.key == K_f:
            Fullscreen = not Fullscreen
            if Fullscreen:
                screen = pygame.display.set_mode((640, 480), FULLSCREEN, 32)
            else:
                screen = pygame.display.set_mode((640, 480), 0, 32)

    screen.blit(background, (0, 0))
    pygame.display.update()

