# -*- coding: utf-8 -*-
"""
Created on Thu May 18 21:19:32 2023

@author: USER
"""

import mysql.connector

conn = mysql.connector.connect(host='127.0.0.1',user='root',passwd='123456789',database='web',auth_plugin='mysql_native_password')

cur = conn.cursor()