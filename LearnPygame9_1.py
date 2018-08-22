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
#记录经过的时间
clock = pygame.time.Clock()
#传入x，y的坐标
position = Vector2(100.0, 100.0)
#heading为Vector2的一个实例对象（self）
heading = Vector2()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.blit(background, (0, 0))
    screen.blit(sprite, position)
    #帧数
    time_passed = clock.tick()
    time_passed_seconds = time_passed/1000.0
    #参数前面加*意味着把列表或元组展开
    destination = Vector2(*pygame.mouse.get_pos()) - Vector2(*sprite.get_size()) / 2
    #计算鱼儿当前位置到鼠标位置的向量
    vector_to_mouse = Vector2.from_points(position, destination)
    #向量规格化（求单位向量）
    vector_to_mouse.normalise()
    # 这个heading可以看做是鱼的速度，但是由于这样的运算，鱼的速度就不断改变了
    # 在没有到达鼠标时，加速运动，超过以后则减速。因而鱼会在鼠标附近晃动。
    heading = heading + (vector_to_mouse * .6)
    #位置随鼠标每帧变换（始终在鼠标周围移动）
    position += heading * time_passed_seconds
    pygame.display.update()
