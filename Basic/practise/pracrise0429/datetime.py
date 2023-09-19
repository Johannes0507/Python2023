# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 01:22:35 2023

@author: 李旻恩
"""

import datetime

# 幾點 幾分 幾秒 幾微秒
time = datetime.time(12,20,20,21)
print(time)
print()

# 幾年 幾月 幾日
d = datetime.date(2023,12,25)
print(d)
print()

# 合併 date and time 
datetime = datetime.datetime(2023,4,29,1,37,20,2000)
print(datetime)
print()

# 顯示現在的時間
now = datetime.datetime.now()
print(now)
print()

# create a timedelta
delta = datetime.timedelta(days=7)
print(delta)  # 7 days, 0:00:00

# perform arithmetic with dates and times
new_date = d + delta
print(new_date)  # 2022-05-08

# format a date or time as a string
print(now.strftime('%Y-%m-%d %H:%M:%S'))  # 2023-04-30 15:25:43
