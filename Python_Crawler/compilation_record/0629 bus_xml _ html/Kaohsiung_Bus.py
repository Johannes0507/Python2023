# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 18:50:12 2023

@author: USER
"""

import requests
import io
import xml.sax

busId = list()
busRoute = list()
busStart = list()
busEnd = list()

class KBusHandler(xml.sax.ContentHandler):
    def startElement(self, tag, attr):
        if tag == "Route":
            busId.append(attr['ID'])
            busRoute.append(attr['nameZh'])
            busStart.append(attr['departureZh'])
            busEnd.append(attr['destinationZh'])

class KBusStop(xml.sax.ContentHandler):
    def startElement(self, tag, attr):
        if tag == "Stop":
            print("站牌:",attr['nameZh'])


if __name__ == '__main__':
    
    parser = xml.sax.make_parser()
    bus = KBusHandler()
    parser.setContentHandler(bus)
    
    url = "https://ibus.tbkc.gov.tw/xmlbus/StaticData/GetRoute.xml"
    
    data = requests.get(url)
    data.encoding = "utf-8"
    data = data.text
    busObj = io.StringIO(data)  # 位元組做解析
    parser.parse(busObj) 

    print('路線:',busId)

    bId = input("請輸入路線:")
    if busId.count(bId) > 0:
        index = busId.index(bId)  # 輸入公車號碼查詢資訊
        print(busId[index])       # 公車號碼
        print(busRoute[index])    # 公車路名
        print(busStart[index])    # 公車起始站
        print(busEnd[index])      # 公車終點站
    else:
        print('找不到此路線！')
    
    # param 參數
    
    routeurl = "https://ibus.tbkc.gov.tw/xmlbus/StaticData/GetStop.xml"
    param = dict()
    param['routeIds'] = bId 
    
    result = requests.get(routeurl,params = param)
    result.encoding = "utf-8"
    result = result.text
    
    Stop = KBusStop()
    parser.setContentHandler(Stop)
    sObj = io.StringIO(result)
    parser.parse(sObj)
    
    print(Stop.text)
    
    # 顯示站牌 去 & 回
    # 提示: 宣告兩個串列,一個去 一個回
    # 顯示：去的公車 車牌 & 回的公車 車牌
    
    
    
    
    
    
    
    
    
    