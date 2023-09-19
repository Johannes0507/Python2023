# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 20:08:46 2023

@author: USER
"""

import requests

import json

import csv

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

number = list()
starttime = list()
endtime = list()
duration = list()


for item in thrs:
    
    number.append(item['TrainNumber'])
    starttime.append(item['DepartureTime'])
    endtime.append(item['DestinationTime'])
    duration.append(item['Duration'])
    

fileName = "thrs.csv"

with open(fileName,'w',encoding='utf-8',newline='') as fO:
    csvWrite = csv.writer(fO)
    csvWrite.writerow(['車次','出發時間','旅行時間','抵達時間'])
    
    for i in range(len(number)):
        csvWrite.writerow([number[i],starttime[i],duration[i],endtime[i]])
    
print('存檔完成')        


    
    









