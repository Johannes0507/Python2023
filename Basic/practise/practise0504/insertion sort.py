# -*- coding: utf-8 -*-
"""
Created on Thu May  4 13:27:38 2023

@author: 李旻恩
"""

Numbers = [41,33,17,80,61,5,55]

length = len(Numbers)
for i in range(1, length):
    position = i
    value = Numbers[i] # 這一行有必要嗎？
    while position > 0 and Numbers[position-1] > Numbers[position]:
        Numbers[position], Numbers[position-1] = Numbers[position-1], Numbers[position]
        position -= 1 # 2的話就是接續 2,1,0 都下去做判斷與交換
        
print(Numbers)