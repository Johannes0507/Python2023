# -*- coding: utf-8 -*-
"""
Created on Tue May 16 20:02:23 2023

@author: USER
"""

import sqlite3

# 資料庫物件
conn = sqlite3.connect('demo.db')



name = input('輸入姓名：')
age = int(input('年齡：'))
sex = input("性別(F/M):")
birth = input('生日(yyyy-mm-dd):')

sql = "insert into students(birthday,sex,name,age) values('{}','{}','{}',{})".format(birth,sex,name,age)

conn.execute(sql)

conn.commit()

conn.close()

