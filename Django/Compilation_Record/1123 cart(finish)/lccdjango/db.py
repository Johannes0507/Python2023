# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 20:11:09 2023

@author: USER
"""

import MySQLdb

conn  = MySQLdb.connect(host='localhost',port=3306,user='root',passwd='1234567890',db='mylcc')

cur = conn.cursor()