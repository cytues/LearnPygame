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

x = 0.
# 速度（像素/秒）
speed = 250.

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.blit(background, (0, 0))
    screen.blit(sprite, (x, 100))
    #上次调用经过的时间
    time_passed = clock.tick()
    time_passed_seconds = time_passed / 1000.0
    #移动距离
    distance_moved = time_passed_seconds * speed
    x += distance_moved

    #区别并不是很大，减去640可能每次的起点不一定是0
    if x > 640.:
        x -= 640

    pygame.display.update()