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
sprite = pygame.image.load(sprite_image_filename).convert_alpha()

clock = pygame.time.Clock()

sprite_pos = Vector2(200, 150)  # 初始位置
sprite_speed = 300.  # 每秒前进的像素数（速度）
sprite_rotation = 0.  # 初始角度
sprite_rotation_speed = 360.  # 每秒转动的角度数（转速）

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    pressed_keys = pygame.key.get_pressed()

    rotation_direction = 0.
    movement_direction = 0.

    # 更改角度
    if pressed_keys[K_LEFT]:
        rotation_direction = +1.
    if pressed_keys[K_RIGHT]:
        rotation_direction = -1.
    # 前进、后退
    if pressed_keys[K_UP]:
        movement_direction = -1.
    if pressed_keys[K_DOWN]:
        movement_direction = +1.

    screen.blit(background, (0, 0))

    # 获得一条转向后的鱼,rotate(Surface, angle) -> Surface
    # 未经过滤的逆时针旋转。 角度参数代表度数并可以是任何浮点值。 负角度量将顺时针旋转。
    rotated_sprite = pygame.transform.rotate(sprite, sprite_rotation)
    # 转向后，图片的长宽会变化，因为图片永远是矩形，为了放得下一个转向后的矩形，外接的矩形势必会比较大
    w, h = rotated_sprite.get_size()
    # 获得绘制图片的左上角
    sprite_draw_pos = Vector2(sprite_pos.x - w / 2, sprite_pos.y - h / 2)
    # 将一个平面的一部分或全部图象整块从这个平面复制到另一个平面
    screen.blit(rotated_sprite, sprite_draw_pos)

    time_passed = clock.tick()
    time_passed_seconds = time_passed / 1000.0

    # 图片的转向速度也需要和行进速度一样，通过时间来控制
    sprite_rotation += rotation_direction * sprite_rotation_speed * time_passed_seconds

    # 获得前进（x方向和y方向），这两个需要一点点三角的知识,类似于sin(pi/6)=30
    heading_x = sin(sprite_rotation * pi / 180.)
    heading_y = cos(sprite_rotation * pi / 180.)
    # 转换为单位速度向量
    heading = Vector2(heading_x, heading_y)
    # 转换为速度
    heading *= movement_direction

    sprite_pos += heading * sprite_speed * time_passed_seconds

    pygame.display.update()