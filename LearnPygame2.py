#-*- coding:utf-8 -*-
#导入相关块
import pygame
from pygame.locals import *
from sys import exit
#初始化
pygame.init()
#窗口大小
SCREEN_SIZE = (640, 480)
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
#设定字体（使用字体模块）这里是默认字体
font = pygame.font.SysFont('arial', 16)
font_heigh = font.get_linesize()
#定义事件列表
event_text = []
#页面循环
while True:
    #只有在发生事件时动，wait的作用
    event = pygame.event.wait()
    #每产生一个事件就添加进列表
    event_text.append(str(event))
    # 这个切片操作保证了event_text里面只保留一个屏幕的文字
    event_text = event_text[-SCREEN_SIZE[1]/font_heigh:]
    #点X退出
    if event.type == QUIT:
        exit()
    #用白色填充背景
    screen.fill((255, 255, 255))
    # 找一个合适的起笔位置，最下面开始但是要留一行的空
    y = SCREEN_SIZE[1]-font_heigh

    for text in reversed(event_text):
        screen.blit(font.render(text, True, (0, 255,0)), (0, y))
        y -= font_heigh
    #刷新
    pygame.display.update()

