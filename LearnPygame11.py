#-*- coding:utf-8 -*-
background_image_filename = './images/sushiplate.jpg'
sprite_image_filename = './images/fugu.png'

import pygame
from pygame.locals import *
from sys import exit
from gameobjects.vector2 import Vector2
from math import *

pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)

background = pygame.image.load(background_image_filename).convert()
sprite = pygame.image.load(sprite_image_filename)

clock = pygame.time.Clock()
# 来完全控制鼠标，这样鼠标的光标看不见，也不会跑到pygame窗口外面去，
# 一个副作用就是无法使用鼠标关闭窗口了，所以你得准备一句代码来退出程序。
# 如果bool参数为true，则鼠标光标将可见。 这将返回光标的前一个可见状态。
pygame.mouse.set_visible(False)#set_visible(bool) -> bool
# set_grab(bool) -> None
# 当您的程序在窗口环境中运行时，它将与其他具有焦点的应用程序共享鼠标和键盘设备。
# 如果您的程序将事件抓取设置为True，它将锁定所有输入到您的程序中。
# 最好不要总是抓住输入，因为它阻止用户在他们的系统上做其他事情。
pygame.event.set_grab(True)

sprite_pos = Vector2(200, 150)
sprite_speed = 300.
sprite_rotation = 0.
sprite_rotation_speed = 360.

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        #检测是否有按键被按下
        if event.type == KEYDOWN:
            #按ESC退出
            if event.key == K_ESCAPE:
                exit()

    pressed_keys = pygame.key.get_pressed()
    pressed_mouse = pygame.mouse.get_pressed()

    rotation_direction = 0.
    movement_direction = 0.
    # get_rel() -> (x, y)
    # 返回自上次调用此函数后X和Y中的移动量。 鼠标光标的相对移动受到屏幕边缘的限制
    rotation_direction = pygame.mouse.get_rel()[0]/5.0

    if pressed_keys[K_LEFT]:
        rotation_direction = +1
    if pressed_keys[K_RIGHT]:
        rotation_direction = -1

    if pressed_keys[K_UP] or pressed_mouse[0]:
        movement_direction = +1
    if pressed_keys[K_DOWN] or pressed_mouse[2]:
        movement_direction = -1

    screen.blit(background, (0, 0))
    # 同样的获得一条转向的鱼
    rotated_sprite = pygame.transform.rotate(sprite, sprite_rotation)
    w, h = rotated_sprite.get_size()
    # 获得图片的左上角
    sprite_draw_pos = Vector2(sprite_pos.x - w / 2, sprite_pos.y - h / 2)
    # 建立一个转向的鱼的图片
    screen.blit(rotated_sprite, sprite_draw_pos)

    time_passed = clock.tick()
    time_passed_seconds = time_passed / 1000.0

    sprite_rotation += rotation_direction * sprite_rotation_speed * time_passed_seconds
    # 获得前进的方向
    heading_x = sin(sprite_rotation * pi / 180.)
    heading_y = cos(sprite_rotation * pi / 180.)
    heading = Vector2(heading_x, heading_y)
    heading *= movement_direction

    sprite_pos += heading * sprite_speed * time_passed_seconds

    pygame.display.update()