# -*- coding: utf-8 -*-
"""
Created on Wed May 24 14:59:33 2023

@author: 李旻恩
"""

import sqlite3

ann = sqlite3.connect("demo.db")

sql = "select sex,name from students "

result = ann.execute(sql)

for row in result:
    print(row[1])
    print(row[0])
    print()
    
ann.commit()

ann.close()