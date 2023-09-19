# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import requests
import json


# json paeser 

url = "https://data.ntpc.gov.tw/api/datasets/71cd1490-a2df-4198-bef1-318479775e8a/json?size=100"

data = requests.get(url).text

bike = json.loads(data)

for row in bike:
    print('站名：',row['sna'])
    print('可借：',row['sbi'])
    print('可停：',row['bemp'])
    print()
    
