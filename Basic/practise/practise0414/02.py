# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 02:28:40 2023

@author: 李旻恩
"""

def circle(r):
    area = r * r * 3.14
    per = 2 * r * 3.14
    return area,per

a = circle(5)

print(a)

b,c = circle(10)

print(b,c)

