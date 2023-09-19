# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 20:43:37 2023

@author: USER
"""

# 字典 

students = {"Tom":98,"David":70,"Mary":6,"Tom":20} # "Tom"的位置是key如果重複的話抓最後面的那一個
print(students["Tom"])                             # :98 的位置是value
# print(students"Bill")
print()

fruit = dict(a = "Apple",b = "Banana")
print(fruit["b"])

print()

number = dict()         # dict() == {}
number[1] = "台中一中"  
number[10] = "台中女中"
print(number)
print(number[10]) 

number[10] = "台中的國立女校"
print(number)

print(students.get("Bill"))
print(students.get("Bill","沒有key"))


