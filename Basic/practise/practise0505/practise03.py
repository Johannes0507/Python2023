# -*- coding: utf-8 -*-
"""
Created on Sat May  6 18:21:13 2023

@author: 李旻恩
"""

import os

myDir = "C:/Users/李旻恩/Desktop/聯成電腦/Python/practise/practise0505/Folder0507"

if os.path.exists(myDir):
    os.rmdir(myDir)
    print('已刪除')

else:
    os.mkdir(myDir)
