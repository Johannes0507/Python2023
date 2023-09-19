# -*- coding: utf-8 -*-
"""
Created on Fri May 12 00:59:05 2023

@author: 李旻恩
"""

import os
for i in range(0):
    os.mkdir('C:\\Users\\李旻恩\\Desktop\\聯成電腦\\Python\\practise\\practise0512')

msg = "Diagnosed with covid-19 today"

with open('msg.txt','w',encoding='utf-8') as fO:
    fO.write(msg)
    