# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 19:50:27 2023

@author: USER
"""

# 算數運算子

a = 5
b = 10 
c = a + b
print(c)
print(a - b)
print(a / b)
print(a * b)
print(a // b)   # 只取整數
print(a % b)    # 只取餘數

print()         # 

#  比較運算子

a = 5
b = 10
print(a > b)
print(a * 2 >= b)
print(a < b)
print(a * 2 == b)
print(a != b)

print()         

# 邏輯運算子

print(a < b and a*2 == b)   # 都成立才成立
print(a > b and a*2 == b)   
print(a > b or a*2 == b)    # 一個對就成立

print(not(a>b))             # not 相反

print()

# 指定運算子 

a = 2
b = 3
a = a + b
b += 2                      # b = b + 2
print(a)
print(b)

a -= 3                      # a = a -3                     
print(a)
a *= b                      # a = a * b
print(a)
a /= b                      # a = a / b
print(a)