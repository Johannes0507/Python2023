# -*- coding: utf-8 -*-
"""
Created on Sat May  6 18:05:40 2023

@author: 李旻恩
"""

studentsName = ['John','Devie','Bill','Peter']
msg = "今天天氣她媽未免也太熱的吧"

fn = "file02.txt"
with open(fn,'a',encoding='utf-8') as f:
    f.write(msg + '\n')
    for item in studentsName:
        f.write(item + '\n')