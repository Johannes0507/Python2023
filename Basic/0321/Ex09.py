# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 21:21:26 2023

@author: USER
"""

for i in range(1,100):
    if i == 20:
        break
    if i % 3 == 0:
        continue
    print(i)
    print("相乘之和",i*i)