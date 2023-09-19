# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 19:03:21 2023

@author: 李旻恩
"""

count = 0
for i in range(1,5):
    for x in range(1,5):
        for y in range(1,5):
            if i != x and i != y and x != y:
                print(i,x,y,end='   ',sep=' ' )
                
                count += 1

print(count)
                



