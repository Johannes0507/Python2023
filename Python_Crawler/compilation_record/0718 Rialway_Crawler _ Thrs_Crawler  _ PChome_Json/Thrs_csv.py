# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 20:03:11 2023

@author: USER
"""

import requests
import json
import csv

url = 'https://www.thsrc.com.tw/TimeTable/Search'
header = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }

param = {
'SearchType': 'S',
'Lang': 'TW',
'StartStation': 'NanGang',
'EndStation': 'ZuoYing',
'OutWardSearchDate': '2023/07/18',
'OutWardSearchTime': '20:30',
'ReturnSearchDate': '2023/07/18',
'ReturnSearchTime': '20:30'    
    
    }

thrs = requests.post(url, headers=header, data=param).text

data = json.loads(thrs)

thrs = data['data']['DepartureTable']['TrainItem']  


Number = list()
StartTime = list()
EndTime = list()
Duration = list()


for item in thrs:
    
    Number.append(item['TrainNumber'])
    StartTime.append(item['DepartureTime'])
    EndTime.append(item['DestinationTime'])
    Duration.append(item['Duration'])
    
fileName = "thrs.csv"
with open(fileName, 'w', newline='') as fO:
    csvWriter = csv.writer(fO)
    csvWriter.writerow(['車次','出發時間','旅行時間','抵達時間'])
    
    for i in range(len(Number)):
        csvWriter.writerow([Number[i],StartTime[i],Duration[i],EndTime[i]])

print('存檔完成')
    
    