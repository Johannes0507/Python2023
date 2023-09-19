# -*- coding: utf-8 -*-
"""
Created on Sun May 14 22:53:35 2023

@author: 李旻恩
"""

import openpyxl

wb = openpyxl.Workbook()

ws = wb.active

ws.title = 'member'

wb.save('lcc.xlsx')