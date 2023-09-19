# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Clothes(object):  # 類別
    def water(self):    # def在類別裡面叫做方法
        return '衣服防潑水'
    def setColor(self,color):
        self.color = color

if __name__ == '__main__':
            
    myClothes = Clothes()
    youClothes = Clothes()
    
    print(id(myClothes))
    print(id(youClothes))
    myClothes.setColor('紅色')
    youClothes.setColor('白色')
    print(myClothes.color)
    print(youClothes.color)   
    my_Clothes = Clothes()     
    print(my_Clothes.water())