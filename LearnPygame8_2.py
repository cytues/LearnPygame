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

# Clock对象
clock = pygame.time.Clock()
#设置初始位置，初始速度
x, y = 100., 100.
speed_x, speed_y = 133.,170.

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.blit(background, (0, 0))
    screen.blit(sprite, (x, y))
    #上次调用经过的时间
    time_passed = clock.tick()
    time_passed_seconds = time_passed / 1000.0
    #鱼每次移动的距离
    x += speed_x * time_passed_seconds
    y += speed_y * time_passed_seconds
    #当x超出右边界时，速度反向，起始点为右边界
    if x > 640 - sprite.get_width():
        speed_x = -speed_x
        x = 640 - sprite.get_width()
    elif x < 0:
        speed_x = -speed_x
        x = 0
    #当y超出上边界时，速度反向，起始点为上边界
    if y > 480 - sprite.get_height():
        speed_y = -speed_y
        y = 480 - sprite.get_height()
    elif y < 0:
        speed_y = -speed_y
        y = 0

    pygame.display.update()