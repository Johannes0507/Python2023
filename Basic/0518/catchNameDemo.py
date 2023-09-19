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
        
        sql = "select * from students where name = '{}' ".format(name)
        cur = conn.cursor()
        cur.execute(sql)
        data = cur.sfetchone()
        print(data)
        
        
        if data == None:
            print('找不到')
            
        else:
            print('姓名：',data[1])
            print('性別：',data[3])
        
finally:
    conn.close()