# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 20:18:35 2023

@author: USER
"""

data = (10,20,30,40)
print(type(data))
print(data[0])

# data[0] = 100 沒辦法新增

listdata = list(data)
listdata[0] = 100

data = tuple(listdata)
print(data)

number = 1,2,3,4,5
print(number)