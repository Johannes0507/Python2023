# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 21:26:41 2023

@author: USER
"""

import copy

data = [100,200,300,400]  # 一維串列

num = copy.copy(data) #淺複製 ，用於一維串列

data.append(10)

print(num)
print(data)