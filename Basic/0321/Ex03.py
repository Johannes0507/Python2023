# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 19:13:02 2023

@author: USER
"""

'''for迴圈'''

print(list(range(10)))
print(list(range(2,10)))
print(list(range(2,10,2)))

"""次數已知都用for迴圈"""

num = int(input("次數："))

total = 0
for i in range(num):     
    print(i)
    total += i
print("總和",total)

num = int(input("階層："))

total = 10
for i in range(1,num+1):     
    print(i)
    total *= i
print("總和：",total)
    
    
    