# -*- coding: utf-8 -*-
"""
Created on Tue May  2 19:20:11 2023

@author: USER
"""

class Role:
    def __init__(self,name,hp):
        self.__name = name
        self.__hp = hp
    
    def fight(self):
        print('角色攻擊')
    
    def display(self):
        print('姓名：',self.__name)
        print('血量：',self.__hp)
        
    def getName(self):
        return self.__name
    
    def changeName(self,name):
        self.__name = name
        
    def HP(self):
        return self.__hp
    
    def changeHP(self,hp):
        self.__hp = hp
        
    
class Adviser(Role):
    def __init__(self,name,hp,level):
        self.level = level
        # 繼承父類別的 name & hp
        super().__init__(name,hp)
        
    def fight(self):
        print('軍師扇扇攻擊')
    
    def cure(self):
        print('治癒自己滿血')

class SwordsMan(Role):
    def fight(self):
        print('大劍一砍')
    
if __name__ == '__main__':
    
    role = Role('關羽',100)
    adviser = Adviser('孔明',200,3)
    man = SwordsMan('張飛',300)    
    
    adviser.fight()
    adviser.cure()
    adviser.display()
    man.display()
    
    # 本來是 self 不能填，但是放進變成物件的adviser後，就可以執行自己類別裡面的東西。
    Role.fight(adviser)
    print()
    
    # print(adviser.hp)      level,hp 因為私有化了所以不能再印出
    # print(adviser.level)
    
    print(adviser.getName())
    adviser.changeName('司馬懿')
    print(adviser.getName())
    
    adviser.changeHP(300)
    print(adviser.HP())

    
    