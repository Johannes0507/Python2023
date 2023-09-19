# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 19:06:35 2023

@author: USER
"""

import re

text = "123大家好abc456ABC"
search = re.search("([0-9]*)大家好([a-z]*)([0-9]*)", text)

# 按照正則表達式裡面的順序去抓取找到內容位置(Ex 0 => ([0-9*]))裡面的內容
for i in range(4):
    print(search.group(i))

print(search.groups())