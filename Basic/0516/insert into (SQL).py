# -*- coding: utf-8 -*-
"""
Created on Tue May 16 20:04:39 2023

@author: USER
"""

import sqlite3


conn = sqlite3.connect('demo.db')
name = input('輸入姓名：')
age = int(input('年齡：'))
sex = input('性別(F/M)：')
birthday = input('生日(yyyy-mm-dd)：')

# 輸入資料代表所對應的資料庫名稱
sql = "insert into students(birthday,name,age,sex) values('{}','{}','{}','{}')".format(birthday,name,age,sex)

conn.execute(sql)

conn.commit()

conn.close()