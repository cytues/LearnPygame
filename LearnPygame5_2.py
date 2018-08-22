#-*- coding:utf-8 -*-
import pygame
from pygame.locals import *
from sys import exit

pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)
#火焰橙和僵尸绿颜色
color1 = (221, 99, 21)
color2 = (96, 130, 51)
#定义factor变量
factor = 0
#颜色变化
def blend_color(color1, color2, blend_factor):
    r1, g1, b1 = color1
    r2, g2, b2 = color2
    r = r1 + (r2 - r1) * blend_factor
    g = g1 + (g2 - g1) * blend_factor
    b = b1 + (b2 - b1) * blend_factor
    return int(r), int(g), int(b)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.fill((255, 255, 255))

    tri = [(0, 120), (639, 100), (639, 140)]
    #在surface上绘制多边形。polygon(Surface, color, pointlist, width=0) -> Rect,
    # pointlist参数是多边形的顶点。 宽度参数是绘制外边缘的厚度。 如果宽度为零，则多边形将被填充。
    pygame.draw.polygon(screen, (0, 255, 0), tri)
    #在surface上绘制圆形。circle(Surface, color, pos, radius, width=0) -> Rect
    #pos参数是圆的中心，radius是半径。 宽度参数是绘制外边缘的厚度。 如果宽度为零，则圆圈将被填充。
    pygame.draw.circle(screen, (0, 0, 0), (int(factor*639.0), 120), 10)
    #x，y的坐标为当前鼠标的坐标
    x, y = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[0]:
        #factor随鼠标的变化而变化
        factor = x / 639.0
        pygame.display.set_caption("Pygame Color Blend Test - %.3f" % factor)
    #每次变化的颜色
    color = blend_color(color1, color2, factor)
    #rect(Surface, color, Rect, width=0) -> Rect，画一个长方形，来显示渐变的颜色
    pygame.draw.rect(screen, color, (0, 240, 640, 240))

    pygame.display.update()

