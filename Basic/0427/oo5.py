# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 21:27:26 2023

@author: USER
"""

class SwordsMan:
    def __init__(self,name,hp,level):
        self.__name = name
        self.__hp = hp
        self.__level = level
        
    def fight(self):
        print(self.__name,'使用三刀流')
        
    def skill(self):
        print(self.__name,'使用星火大亂砍')
    
    def changeHp(self,hp):
        self.__hp -= hp
        return self.__hp
   
    def getHp(self):
        return self.__hp
    
    def getName(self):
        return self.__name
    
    
class Dancer:
    def __init__(self,name,hp,level):
        self.__name = name
        self.__hp = hp
        self.__level = level
        
    def fight(self):
        print(self.__name,'國標舞')
        
    def skill(self):
        print(self.__name,'胡桃鉗舞曲')
    
    def cure(self):
        print('我來補血囉！！')
    
    def changeHp(self,hp):
        self.__hp -= hp
        return self.__hp
   
    def getHp(self):
        return self.__hp
    
    def getName(self):
        return self.__name
    
class Adviser:
    def __init__(self,name,hp,level):
        self.__name = name
        self.__hp = hp
        self.__level = level
        
    def fight(self):
        print(self.__name,'使出扇子攻擊')

    def skill(self):
        print(self.__name,'火龍計')

    def cure(self):
        print(self.__name,'使出補血')
    
    def trick(self):
        print(self.__name,'水淹七軍')
    
    def changeHp(self,hp):
        self.__hp -= hp
        return self.__hp
   
    def getHp(self):
        return self.__hp
    
    def getName(self):
        return self.__name
        
        
    