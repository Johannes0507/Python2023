# -*- coding: utf-8 -*-
"""
Created on Tue May  2 21:03:05 2023

@author: USER
"""

# 抽象繼承 (不能生成)
# 用程式來規範子類別一定要寫完整方法

from abc import ABCMeta,abstractmethod

class Person(metaclass = ABCMeta):
    # 未完成的"方法"就是未完成的"類別"
    @abstractmethod
    def display(self,name):
        pass
    
    def pay(self):
        self.display(self.name,self.salary)
        
class Clerk(Person):
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    
    def display(self,name,salary):
        print(name,'是Clerk')
        print('薪水：',salary)
        
bill = Clerk('Bill',2000)

bill.pay()

# 輸出會寫抽象類別無法被生成
p = Person()



