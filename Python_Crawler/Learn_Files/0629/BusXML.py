# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
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
            
            
class kBusStop(xml.sax.ContentHandler):
    def startElement(self,tag,attr):
        if tag == "Stop":
            print("站牌：",attr['nameZh'])



if __name__ == "__main__":
    parser = xml.sax.make_parser()
    bus = KBusHandler()
    parser.setContentHandler(bus)
    
    url = "https://ibus.tbkc.gov.tw/xmlbus/StaticData/GetRoute.xml"
    
    data = requests.get(url)
    data.encoding = "utf-8"
    data = data.text
    busObj = io.StringIO(data)
    parser.parse(busObj)
    
    print("路線：",busId)
    
    bId = input("請輸入路線：")
    if busId.count(bId) > 0:
        index = busId.index(bId)
        print(busId[index])
        print(busRoute[index])
        print(busStart[index])
        print(busEnd[index])
        
    routeurl = "https://ibus.tbkc.gov.tw/xmlbus/StaticData/GetStop.xml"    
    param = dict()
    param['routeIds'] = bId
    
    result = requests.get(routeurl,params=param)
    result.encoding = "utf-8"
    result = result.text
    
    Stop = kBusStop()
    parser.setContentHandler(Stop) # 這裡的parser用來
    sObj = io.StringIO(result)
    parser.parse(sObj)
    
    
    # 顯示去 -> 站牌   回-> 站牌
    
    # 提示：可宣告二個串列 ，一個記錄去  ，一個記錄回
    
    # 再顯示：去的公車的車牌有那些  回的公車車牌有那些
    
    
    
    
        
 
    
    
    
    
    
    

            
        
        
        
        
        
        