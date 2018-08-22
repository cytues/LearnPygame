#-*- coding:utf-8 -*-
#指向背景图和光标图片
background_image_filename = './images/sushiplate.jpg'
mouse_image_filename = './images/fugu.png'
#导入相关模块
import pygame
#导入一些常用函数
from pygame.locals import *
#退出函数
from sys import exit
#初始化pygame
pygame.init()
#创建了一个长为640宽480的窗口来显示游戏界面
screen = pygame.display.set_mode((640, 480), 0, 32)
#设置窗口标题
pygame.display.set_caption("Hello, World!")
#image.load用来加载图片
background = pygame.image.load(background_image_filename).convert()
mouse_cursor = pygame.image.load(mouse_image_filename).convert_alpha()
#游戏主循环
while True:
    #点×退出程序
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    #blit将背景图画到窗口上
    screen.blit(background, (0,0))
    #获得鼠标位置
    x, y = pygame.mouse.get_pos()
    #定位光标左上角，开始时光标在窗口中间
    x -= mouse_cursor.get_width() / 2
    y -= mouse_cursor.get_height() / 2
    #把光标画上去
    screen.blit(mouse_cursor, (x, y))
    #刷新画面
    pygame.display.update()
