# -*- coding: utf-8 -*-
"""
Created on Tue May 16 20:50:22 2023

@author: USER
"""

import sqlite3

conn = sqlite3.connect('demo.db')

# 查詢 *所有欄位，ex: name、sex、age.... 來自 'students'
sql = "select * from students"

result = conn.execute(sql)

# print(list(result))

for row in result:
    print(row[0],'姓名：',row[1])
    print('性別：',row[3])
    print()
    
    
conn.commit()

conn.close()