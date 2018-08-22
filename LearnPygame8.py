#-*- coding:utf-8 -*-
background_image_filename = './images/sushiplate.jpg'
sprite_image_filename = './images/fugu.png'

import pygame
from pygame.locals import *
from sys import exit

pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)

background = pygame.image.load(background_image_filename).convert()
sprite = pygame.image.load(sprite_image_filename)
#sprite起始坐标
x = 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.blit(background, (0, 0))
    #画出sprite
    screen.blit(sprite, (x, 100))
    #每循环一次移动1个像素
    x += 1
    #若超出边界则从头开始
    if x > 640:
        x = 0

    pygame.display.update()
