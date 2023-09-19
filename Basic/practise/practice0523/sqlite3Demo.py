# -*- coding: utf-8 -*-
"""
Created on Tue May 23 00:57:07 2023

@author: 李旻恩
"""

import sqlite3

conn = sqlite3.connect('demo.db')

# id 欄位名稱 "sqlite如果是autoincrement 的話前面整數要用integer"
sql = "create table if not exists students(id integer primary key autoincrement,name varchar(30),age int,sex varchar(2),birthday varchar(10))"

conn.execute(sql)

# 立即生效
conn.commit()

conn.close()

