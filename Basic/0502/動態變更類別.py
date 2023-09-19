# -*- coding: utf-8 -*-
"""
Created on Tue May  2 21:31:58 2023

@author: USER
"""

class Father:
    def display(self,name):
        self.name = name
        print('Father name is：',self.name)
    
class Mother:
    def display(self,name):
        self.name = name
        print('Mother name is：',self.name)

class Child(Father,Mother):
    pass

class Son(Father):
    pass

print(Child.__name__,'繼承')  
for item in Child.__bases__: # 印出Child繼承誰
    print(item)
    
print()
print(Son.__name__,'繼承')
print(Son.__bases__)    # 用元祖印出Son被什麼繼承

son = Son()
son.display('David')

Son.__bases__ = (Mother,)   # 把son變成繼承Mother 
son.display('Mary')