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
        
        print(data)
        
        if len(data) == 0:
            print('找不到')
        
        else:
            for row in data:
                print('ID：',row[0])
                print('name：',row[1])
                print('age：',row[2])
                print('sex：',row[3])
                print()
            
            q = input(' 修改資料 => 1 刪除資料 => 2 不變更 => n：')
            
            # 修改資料表
            if q == '1':
                    
                num = int(input('請輸入欲修改的ID：'))
                age = int(input('請輸入欲修改的Age：'))
                sql = "update students set age={} where id={}".format(age,num)
                cur.execute(sql)
                conn.commit()
                
                
            # 刪除資料表
            elif q == '2':
                
                num = int(input('輸入欲刪除的ID：'))
                sql = "delate from students where id={}".format(num)
                cur.excute(sql)
                conn.commit()
                
                
                                
finally:
    conn.close()