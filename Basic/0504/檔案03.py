# -*- coding: utf-8 -*-
"""
Created on Thu May  4 19:35:30 2023

@author: USER
"""

fn = "file02.txt"
with open(fn,encoding='UTF-8') as fObj:
    for line in fObj:
        print(line)
        print('-'*30)