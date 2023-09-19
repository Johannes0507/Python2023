# -*- coding: utf-8 -*-
"""
Created on Tue May  2 20:39:18 2023

@author: USER
"""

class A:
    def aMethod(self):
        print('aMethod')

class B(A):
    def bMethod(self):
        print('bMethod')
    
    def display(self):
        print('b-display')

class C(B):
    def cMethod(self):
        print('cMethod')
    
    def display(self):
        print('c-display')

class D(C,B):
    def dMethod(self):
        print('dMethod')
 
a = C()

a.aMethod()
a.bMethod()
a.display()

# 有一樣方法時，會先繼承先輸入的那個方法。 ex:D(C,B) 會先繼承一樣方法的C
d = D()
d.display()

