# -*- coding: utf-8 -*-
"""
Created on Tue May 23 21:20:08 2023

@author: USER
"""

import db

print("Ubike")

while True:
    num = input('1  2  3  q:')
    if num == 'q':
        break
    
    if num == '1':
        station = input('Station:')
        sql = "select * from ntpbike where station like '%{}%'".format(station)
        
    elif num == '2':
        sql = "select distinct area from ntpbike"
        db.cur.execute(sql)
        data = db.cur.fetchall()
        for row in data:
            print(row[0],end=',')
        print()    
        
        area = input('Area:')
        sql = "select * from ntpbike where area='{}'".format(area)
        
    db.cur.execute(sql)    
    data = db.cur.fetchall()
    for row in data:
        print(row[1],row[3],row[4])
        
        
        
        
        
    
db.conn.close()    
    