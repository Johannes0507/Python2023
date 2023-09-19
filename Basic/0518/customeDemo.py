# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import sqlite3

conn = sqlite3.connect("demo.db")


try:
    while True:
        name = input('請輸入姓名，q離開：')
        
        if name == 'q':
            break
        
        sql = "select * from students where name like '%{}%' ".format(name)
        cur = conn.cursor()
        cur.execute(sql)
        data = cur.fetchall()
        
        if data == None:
            print('找不到')
            
        else:
            for row in data:
                print('name：',row[1])
                print('age：',row[2])
                print('sex：',row[3])
                print()
                
        
finally:
    conn.close()