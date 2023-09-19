# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 19:17:52 2023

@author: USER
"""

import db

sql = "select * from product"

db.cur.execute(sql)