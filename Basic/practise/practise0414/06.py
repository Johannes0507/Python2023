# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 16:51:21 2023

@author: 李旻恩
"""

def showStudents(*stud):
    for items in stud:
        print("學生:",items)
    print()

showStudents()

showStudents("Bill","Mary","John","Keven")

def employee(name,pay,*work,area="台北"):
    print("姓名：",name)
    print("薪資：",pay)
    for items in work:
        print("工作項目：",items)
    print("工作地：",area)

a = employee("Bill",2000,"文書處理","上網","睡覺","玩遊戲","台北")
        
print(a)

