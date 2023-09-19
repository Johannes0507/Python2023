# -*- coding: utf-8 -*-
"""
Created on Thu May  4 19:26:35 2023

@author: USER
"""

fn = "file02.txt"
with open(fn,encoding='UTF-8') as fobj: # open 打開檔案文字類型是UTF-8 在 fobj
    data = fobj.read()

print(data)