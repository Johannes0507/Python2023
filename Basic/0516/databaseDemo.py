# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import sqlite3

# 建立物件
conn = sqlite3.connect('demo.db')

# autoincrement 流水編號
# if not exists 如果沒有此檔案就建立
sql = "create table if not exists students(id integer primary key autoincrement, name varchar(30), age int, sex varchar(2), birthday carchat(10))"

# 執行
conn.execute(sql)

# 立即生效
conn.commit()

# 關閉
conn.close()