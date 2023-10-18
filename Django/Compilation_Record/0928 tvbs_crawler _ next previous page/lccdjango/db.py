# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 18:54:23 2023

@author: USER
"""

import MySQLdb as sql

conn = sql.connect(
    host='KeithLee',
    port=3306,
    user='root',
    passwd='050757johannes',
    db='mylcc'
    )

cur = conn.cursor()