#-*- coding:utf-8 -*-
import pygame
from pygame.locals import *
from sys import exit

pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)


def create_scales(height):
    #创建一个surface对象，传入长和宽
    red_scale_surface = pygame.surface.Surface((640, height))
    green_scale_surface = pygame.surface.Surface((640, height))
    blue_scale_surface = pygame.surface.Surface((640, height))
    for x in range(640):
        c = int((x / 640.) * 255.)
        red = (c, 0, 0)
        green = (0, c, 0)
        blue = (0, 0, c)
        #创建一个矩形对象，前面两个参数是矩形左上角定点的坐标，后面两个参数分别是宽和高
        line_rect = Rect(x, 0, 1, height)
        #在surface上画某个矩形框，第一个参数是母surface，第二个参数是颜色，第三个参数是矩形框对象或者四个值
        pygame.draw.rect(red_scale_surface, red, line_rect)
        pygame.draw.rect(green_scale_surface, green, line_rect)
        pygame.draw.rect(blue_scale_surface, blue, line_rect)
    return red_scale_surface, green_scale_surface, blue_scale_surface

#画出高为80的三个三原色长方形
red_scale, green_scale, blue_scale = create_scales(80)

color = [127, 127, 127]

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.fill((0, 0, 0))

    screen.blit(red_scale, (0, 00))
    screen.blit(green_scale, (0, 80))
    screen.blit(blue_scale, (0, 160))

    x, y = pygame.mouse.get_pos()
    #如果鼠标被按下
    if pygame.mouse.get_pressed()[0]:
        for component in range(3):
            if y > component * 80 and y < (component + 1) * 80:
                color[component] = int((x / 639.) * 255.)
        #标题显示三原色的数值
        pygame.display.set_caption("PyGame Color Test - " + str(tuple(color)))

    for component in range(3):
        #圆的位置
        pos = (int((color[component] / 255.) * 639), component * 80 + 40)
        #画三个白色的圆，第一个参数为surface对象，第二个参数为颜色，第三个参数为圆心的坐标，第四个参数为半径
        pygame.draw.circle(screen, (255, 255, 255), pos, 20)
    #画出显示色彩的长方形
    pygame.draw.rect(screen, tuple(color), (0, 240, 640, 240))

    pygame.display.update()