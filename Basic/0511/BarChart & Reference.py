# -*- coding: utf-8 -*-
"""
Created on Sun May 14 23:25:18 2023

@author: 李旻恩
"""

import openpyxl

from openpyxl.chart import BarChart,Reference

wb = openpyxl.Workbook()

ws = wb.active

sales = [['區域','2021年','2022年'],['台北',31000,29100]['台中',49800,30000]['高雄',35700,45600]]

for row in sales:
    ws.append(row)
    
chart = BarChart()
chart.title = "各區銷售額"
chart.x_axis.title = "地區" 
chart.y_axis.title = "金額"

# 建立圖表
data = Reference(ws,min_col=2,max_col=3,min_row=1,max_row=4)
chart.add_data(data,titles_from_data=True)

xtitle = Reference(ws,min_col=1,min_row=2,max_row=4)
chart.set_categories(xtitle)

    
