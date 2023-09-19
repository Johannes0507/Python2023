# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 20:56:21 2023

@author: USER
"""

import requests
import xml.sax


# ContentHandler 處理內容
class bikeXML(xml.sax.ContentHandler):
    
    def __init__(self):
        self.station = ""
        self.sbi = ""
        self.bemp = ""
    
    def startElement(self, tag, attr):
        self.tag = tag
        
    def characters(self, content):
        if self.tag == 'sna':
            self.station = content
        if self.tag == 'sbi':
            self.sbi == content
        if self.tag == 'bemp':
            self.bemp == content
        
    def endElement(self, tag):
        if self.tag == 'sna':
            print('站名', self.station)
        if self.tag == 'sbi':
            print('可借', self.sbi)
        if self.tag == 'bemp':
            print('可停', self.bemp)



if __name__ == '__main__':
    
    parser = xml.sax.make_parser()
    bike = bikeXML()
    parser.setContentHandler(bike)
    
    url = "https://data.ntpc.gov.tw/api/datasets/71cd1490-a2df-4198-bef1-318479775e8a/xml?size=100"
    
    data = requests.get(url)
    data.encoding = 'utf - 8'
    data = data.text
    fname = 'bike.xml'
    
    with open(fname, 'w', encoding = 'utf - 8') as fObj:
        fObj.write(data)
    
    parser.parse(fname)
    
    
    