# -*- coding: utf-8 -*-
"""
Created on Fri May  5 17:56:55 2023

@author: 李旻恩
"""

fn = "file01.txt"

msg = "今天天氣好熱！"
data = ['Bill','John','Johannes']

with open(fn,'w',encoding='utf-8') as fObj:
    fObj.write(msg + '\n')
    for line in data:
        fObj.write(line + '\n')
        
            