# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def sayHello(name):
    print(name,'你好')
    
# **x -> x等於 
def square(x):
    return x ** 2

sayHello('Bill')
print(square(5))

print('-'*30)

# lambda 第一種寫法
(lambda name:print(name,'你好'))('John')

# lambsa 第二種寫法
sq = lambda x:x ** 2
print(sq(5))

# lambda可以帶入不只一個數值
sq2 = lambda x,y : x*y
print(sq2(2,3))