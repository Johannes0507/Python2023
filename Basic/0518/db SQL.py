# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import db

try:
    while True:
        name = input('請輸入姓名，q離開：')
        
        if name == 'q':
            break
        
        sql = "select * from students where name = '{}' ".format(name)
    
        db.cur.execute(sql)
        data = db.cur.fetchone()
        print(data)
        
        
        if data == None:
            print('找不到')
            
        else:
            print('姓名：',data[1])
            print('性別：',data[3])
        
finally:
    db.conn.close()