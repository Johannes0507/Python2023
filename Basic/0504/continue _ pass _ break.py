# -*- coding: utf-8 -*-
"""
Created on Thu May  4 18:50:43 2023

@author: USER
"""

for i in range(20):
    if i == 10:
        break
    if i % 4 == 0:
        continue # 掠過一次
    if i == 3:
        pass
    print(i)