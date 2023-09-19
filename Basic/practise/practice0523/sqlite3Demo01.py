# -*- coding: utf-8 -*-
"""
Created on Wed May 24 12:01:13 2023

@author: 李旻恩
"""

import sqlite3

# 資料庫物件
conn = sqlite3.connect("demo.db")

name = input('輸入姓名：')

age = int(input('年齡：'))

sex = input('性別(F/M)：')

birthday = input('輸入生日(yyyy-mm-dd)：')

sql = "insert into students(birthday,sex,age,name) values('{}','{}','{}','{}')".format(birthday,sex,age,name)

conn.execute(sql)

conn.commit()

conn.close()