# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 21:27:58 2023

@author: USER
"""

class SwordMan:
    
    def __init__(self,name,hp,mp):
        self.__name = name
        self.__hp = hp
        self.__mp = mp
        
    def fight(self):
        print(self.__name,'使出三刀流')
        
    def skill(self):
        print(self.__name,'使出星爆大亂砍')
        
    def changeHp(self,hp):
        self.__hp -= hp
        return self.__hp
    
    def egtHp(self):
        return self.__hp
    

class Dancer:
    
    def __init__(self,name,hp,mp):
        self.__name = name
        self.__hp = hp
        self.__mp = mp
        
    def fight(self):
        print(self.__name,'跳舞')
        
    def skill(self):
        print(self.__name,'坐著跳舞')
        
    def changeHp(self,hp):
        self.__hp -= hp
        return self.__hp
    
    def egtHp(self):
        return self.__hp