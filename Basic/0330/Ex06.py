# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 21:38:20 2023

@author: USER
"""

fruit = {"apple":34,"orange":68,"banana":49}
fruit["orange"] = 168
print(fruit)
print()

del fruit["apple"]  # del == 刪除 
print(fruit)
print()

fruit.clear()   # clear == 全部清除
print(fruit)