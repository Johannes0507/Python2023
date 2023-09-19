# -*- coding: utf-8 -*-
"""
Created on Thu May  4 21:28:17 2023

@author: USER
"""

fn = "file02.txt"

with open(fn,encoding='utf-8') as f:
    data = f.read()
    newdata = data.replace('基礎概念','中級概念')
    print(newdata.strip())
    
with open("news.txt",'w',encoding = 'utf-8') as f:
    f.write(newdata.strip())