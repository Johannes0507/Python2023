# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 20:32:11 2023

@author: USER
"""

number = [99,66,33,45,64,89,80]

number.sort() #小至大
print(number)

number.sort(reverse=True)
print(number)

print()

number = [99,66,33,45,64,89,80]

newNum = sorted(number)

print(newNum)
print(number)

print()

newNum2 = sorted(number,reverse=True)
print(newNum2)
print(number)