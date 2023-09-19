# -*- coding: utf-8 -*-
"""
Created on Sun May  7 18:06:19 2023

@author: 李旻恩
"""
from datetime import datetime
import sys
import traceback

def writeLog(errMsg):
    now = datetime.now()
    happen = now.strftime('%H:%M:%S')
    fileName = now.strftime('%Y %m %d') + '.log'
    with open(fileName,'a',encoding='utf-8') as fObj:
        fObj.write(happen + " " + errMsg + '\n')

data = ['Python','jQL','JavaScripe']

try:
    print(data[0])
    print(data[3])
    
except Exception as ex:
    cl,eQ,tb = sys.exc_info()
    lastCallStack = traceback.extract_tb(tb)[-1]
    
    fileName = lastCallStack[0]
    lineName = lastCallStack[1]
    fucName = lastCallStack[2]
    
    msg = ex.args[0]
    error = "File：{},Line：{},Detail：{}".format(fileName,lineName,msg)
    writeLog(error)


    
    
    