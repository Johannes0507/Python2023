# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 20:08:46 2023

@author: USER
"""

import requests

import json

url = "https://www.thsrc.com.tw/TimeTable/Search"

header = {
    'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }

param = {
'SearchType': 'S',
'Lang': 'TW',
'StartStation': 'NanGang',
'EndStation': 'ZuoYing',
'OutWardSearchDate': '2023/07/18',
'OutWardSearchTime': '20:00',
'ReturnSearchDate': '2023/07/18',
'ReturnSearchTime': '20:00'
    }


thrs = requests.post(url,headers=header,data=param).text

data = json.loads(thrs)

thrs = data['data']['DepartureTable']['TrainItem']


for item in thrs:
    
    print("車次：",item['TrainNumber'])
    print("出發時間：",item['DepartureTime'])
    print("旅行時間：",item['Duration'])
    print("抵達時間：",item['DestinationTime'])
    print("停靠站")
    
    print()
    
    









