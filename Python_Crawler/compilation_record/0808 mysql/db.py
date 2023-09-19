# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 21:01:13 2023

@author: USER
"""

import mysql.connector

# 輸入要傳輸的參數 auth_plugin 為認證憑證 (不可省略)
conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '1234567890',
    database = 'myweb',
    auth_plugin = 'mysql_native_password'
    )
# data set
cur = conn.cursor()