# -*- coding: utf-8 -*-
"""
Created on Thu May  4 13:25:00 2023

@author: 李旻恩
"""

Numbers = [41,33,17,80,61,5,55]

length = len(Numbers)

for i in range(length-1):
    min_index = i
    
    for j in range(i+1, length):
        if Numbers[min_index] > Numbers[j]:
            min_index = j
    Numbers[min_index], Numbers[i] = Numbers[i], Numbers[min_index]
    
print(Numbers)