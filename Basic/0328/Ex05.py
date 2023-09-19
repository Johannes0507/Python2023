# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 20:55:45 2023

@author: USER
"""

a = 10

b = a

number = [10,20,30,40]

num = number

print(a)
print(b)
print(number)
print(num)
print()
print(id(a))
print(id(b))
print(id(number))
print(id(num))
print()

a = 100
print(b)
print(id(a))
print(id(b))
print(id(number))
print(id(num))

number[0] = 100
print(num)
print(id(a))
print(id(b))
print(id(number))
print(id(num))





