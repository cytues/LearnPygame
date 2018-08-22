#-*- coding:utf-8 -*-
background_image_filename = './images/sushiplate.jpg'
sprite_image_filename = './images/fugu.png'

import pygame
from pygame.locals import *
from sys import exit
from gameobjects.vector2 import Vector2

pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)

background = pygame.image.load(background_image_filename).convert()
sprite = pygame.image.load(sprite_image_filename)

clock = pygame.time.Clock()
#传入坐标被作为向量
sprite_pos = Vector2(200, 150)
#初始速度
sprite_speed = 300.

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    #获取按下的键值
    pressed_keys = pygame.key.get_pressed()
    #设置按键的向量初值
    key_direction = Vector2(0, 0)
    #若按下左键则像素减一
    if pressed_keys[K_LEFT]:
        key_direction.x = -1
    elif pressed_keys[K_RIGHT]:
        key_direction.x = 1
    if pressed_keys[K_UP]:
        key_direction.y = -1
    elif pressed_keys[K_DOWN]:
        key_direction.y = 1
    #按键向量规格化
    key_direction.normalize()

    screen.blit(background, (0, 0))
    screen.blit(sprite, sprite_pos)

    time_passed = clock.tick(30)
    time_passed_passed = time_passed / 1000.0
    #鱼的新的位置=（按键向量*鱼的运动速度*帧）+ 初始位置（前一个位置）
    sprite_pos += key_direction * sprite_speed * time_passed_passed
    #刷新鱼图片位置
    pygame.display.update()