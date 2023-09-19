# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 22:22:28 2023

@author: 李旻恩
"""

import math 

class Circle:
    def __init__(self,radius = 6):
        self.radius = radius

    def roundArea(self):
        return self.radius * self.radius * math.pi
    
    def colcPerimeter(self):
        return self.radius * 2 * math.pi
    
if __name__ == '__main__':
    
    circle = Circle(12)
    
    print('半徑：',circle())
    print('圓周長：{:.2f}'.format(circle.colcPerimeter()))
    print('圓面積：{:.2f}'.format(circle.roundArea()))
    
    