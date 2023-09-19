# -*- coding: utf-8 -*-
"""
Created on Thu May  4 19:50:17 2023

@author: USER
"""

fn = "file04.txt"
msg = "今天晚餐的餐廳變不好吃了."
data = ["聯成電腦","電腦","Python"]
with open(fn,'a',encoding='utf-8') as f:    # a等於複寫
    f.write(msg + '\n')
    for line in data:
        f.write(line + '\n')
        
        