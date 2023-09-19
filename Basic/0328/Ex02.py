# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 19:52:12 2023

@author: USER
"""

students = ['David','Bill','Mary','Peter']

# remove 裡面的元素一定要在串列中。不然會發生Error
students.remove("Bill")

print(students)

if students.count("Tom") > 0:

    students.remove("Tom")
    
    
#pop  取出不放回    

print()

number = [1,2,3,4,5,6,7,8]

number.pop()

# print(n)
print(number)

n = number.pop(5)
print(n)
print(number)

# number.pop(15)


