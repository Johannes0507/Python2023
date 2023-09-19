# -*- coding: utf-8 -*-
"""
Created on Tue May  2 19:20:11 2023

@author: USER
"""

class Role:
    def __init__(self,name,hp):
        self.name = name
        self.hp = hp
    
    def fight(self):
        print('角色攻擊')
    
    def display(self):
        print('姓名：',self.name)
        print('血量：',self.hp)
    
class Adviser(Role):
    def fight(self):
        print('軍師扇扇攻擊')
    
    def cure(self):
        print('治癒自己滿血')

class SwordsMan(Role):
    def fight(self):
        print('大劍一砍')
    
if __name__ == '__main__':
    role = Role('關羽',100)
    adviser = Adviser('孔明',200)
    man = SwordsMan('張飛',300)    
    
    adviser.fight()
    adviser.cure()
    adviser.display()
    man.display()
    
    # 本來是self不能填但是放進變成物件的adviser就可以執行自己類別面的東西。
    Role.fight(adviser)