#-*- coding:utf-8 -*-
import math

class Vector2(object):
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y
    #字符串方法
    def __str__(self):
        return "(%s, %s)" % (self.x, self.y)
    #加法
    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)
    #减法
    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)
    #乘法
    def __mul__(self, scalar):
        return Vector2(self.x * scalar, self.y * scalar)
    #除法
    def __div__(self, scalar):
        return Vector2(self.x / scalar, self.y / scalar)
    #用修饰器继承类的方法
    @classmethod
    #计算向量
    def from_points(cls, p1, p2):
        return cls(p2[0] - p1[0], p2[1] - p1[1])
    #计算向量的模
    def sq(self):
        return math.sqrt(self.x**2 + self.y**2)
    #将向量除以它的模后,所得的向量就是它的单位向量
    def normalize(self):
        magnitude = self.sq()
        self.x /= magnitude
        self.y /= magnitude


A = (10.0, 20.0)
B = (30.0, 50.0)

AB = Vector2.from_points(A, B)
print(AB)