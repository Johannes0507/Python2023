# -*- coding: utf-8 -*-
"""
Created on Thu May  4 19:40:32 2023

@author: USER
"""

fn = "file02.txt"

with open(fn,encoding='utf-8') as fObj:
    
    data = fObj.readline() # 只讀一行
    print(data)
    print()
    
    datas = fObj.readlines()    # 每次讀一行並存入list中
    print(datas)
    print()
    
    text = fObj.readable()
    print(text)
    print()
    
for line in datas:
    print(line.strip()) # 去除前後空白