# -*- coding: utf-8 -*-
"""
Created on Tue May 16 20:50:22 2023

@author: USER
"""

import sqlite3

conn = sqlite3.connect('demo.db')

# 查詢 *所有欄位，ex: name、sex、age.... 來自 'students'

# sql = " select * from students "

# sql = " select * from students where sex = 'F' "

# sql = " select * from students where sex = 'F' and age > 20 and age < 50 "

# age between 20 and 50 條件找出 age 20 ~ 50 之間的人
sql = " select * from students where sex = 'F' and age between 20 and 50 "


# cursor 資料集
cursor = conn.cursor()

cursor.execute(sql)

result = cursor.fetchall()

print(list(result))

conn.close()