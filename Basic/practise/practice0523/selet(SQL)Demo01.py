# -*- coding: utf-8 -*-
"""
Created on Wed May 24 14:59:33 2023

@author: 李旻恩
"""

import sqlite3

ann = sqlite3.connect("demo.db")

# sql = "select * from students where sex = 'F'"

# sql = "select * from students where sex = 'F' and age <= 25"

# sql = "select * from students where sex = 'F' and age > 20 and age < 25"

# between 介於 只能用日期跟整數
sql = "select * from students where age between 20 and 25"

cursor = ann.cursor()

res = cursor.execute(sql)

for row in res:
    print(row[1])
    print(row[2])
    print()

ann.commit()

ann.close()