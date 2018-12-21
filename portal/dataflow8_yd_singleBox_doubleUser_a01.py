# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 15:59:53 2018

这个是盒子+CDN的场景
CDN
|
Box1          Box2
|              |
User1 User2   User3 User4

@author: Administrator
"""
import mysql.connector
import numpy as np
import time
import struct
import pandas as pd
import random

def sqlGe(SourceCategory,DesCategory,SourceID,DestID,TotalData,DateTime,DestMac,SourceMac):
    valueCon= {}
    valueCon["ID"] = "Default"
    valueCon["SourceCategory"] = SourceCategory
    valueCon["DesCategory"] = DesCategory
    valueCon["SourceID"] = SourceID
    valueCon["DestID"] = DestID
    valueCon["TotalData"] = TotalData
    valueCon["DateTime"] = DateTime
    valueCon["DestMac"] = DestMac
    valueCon["SourceMac"] = SourceMac
    
    addFlow = """insert into dataflow_info values (
         %(ID)s,
         %(SourceCategory)d,
         %(DesCategory)d,
         \"%(SourceID)s\",
         \"%(DestID)s\",
         %(TotalData)d,
         \"%(DateTime)s\",
         \"%(DestMac)s\",
         \"%(SourceMac)s\"
         )"""%valueCon
    return addFlow

def InsertToMysql():

    conn = mysql.connector.connect(user="root", password="root", 
                                   host="47.94.34.61", database="mecs")    
    cur = conn.cursor()
    
    timeRange = pd.date_range('2018-12-08 10:00:22', '2018-12-08 10:30:00', freq= '80min')
    
    
    
    d1000 = {}
    d1000["A4:44:D1:1B:5A:A1"] = "A4:44:D1:1B:5A:A1"
    d1000["D8:63:75:25:67:80"] = "D8:63:75:25:67:80"
    
    d2000 = {}
    d2000["1000000"] = ["1000001"]

    
    dev_map = {}
    dev_map["1000000"] = "22:31:0f:8e:99:2a"
    dev_map["1000001"] = "02:81:28:f8:c7:d5"
    dev_map["1000003"] = "02:81:28:f8:c7:d6"
    dev_map["1000004"] = "02:81:28:f8:c7:d7"
    dev_map["1000005"] = "02:81:28:f8:c7:d8"
    dev_map["1000013"] = "02:81:f6:cf:1c:f2"
    dev_map["1000014"] = "02:81:5d:ab:98:14"
    dev_map["1000018"] = "02:81:66:b3:e2:af"
    dev_map["1000022"] = "02:81:8c:e3:fc:48"
    
    maindev = "1000018"
    bakdev = "1000022"
    
    usr1 = "37353925-6BE22460-4B26CA00-ttx"
    usr2 = "37353925-6BE22460-4B26CA00-ttx2"
    
    usr3 = "37353925-6BE22460-4B26CA00-xsj"
    usr4 = "37353925-6BE22460-4B26CA00-xsj2"
    
    
    onePack = 100000000000;
    
    for i in timeRange:
        if onePack < 0:
            TotalData = 0
            cur.close()
            conn.close()
            return
        else:
            TotalData = random.randint(0,200000000)
            if (onePack - TotalData) > 0:
                onePack = onePack - TotalData
            else:
                TotalData = onePack
                onePack = -1      
        DateTime = str(i)
    
        
        tmpVal = random.randint(0,1)
        if tmpVal == 0:
            SourceCategory = 2000
            DesCategory = 1200
            SourceID = "1000000"
            DestID = usr1
            DestMac = d1000[DestID]
            SourceMac = dev_map[SourceID]
            addFlow = sqlGe(SourceCategory,DesCategory,SourceID,DestID,TotalData,DateTime,DestMac,SourceMac)
            
        
        else:
            SourceCategory = 2000
            DesCategory = 1000
            SourceID = "1000000"
            DestID = maindev
            DestMac = dev_map[DestID]
            SourceMac = dev_map[SourceID]
            addFlow = sqlGe(SourceCategory,DesCategory,SourceID,DestID,TotalData,DateTime,DestMac,SourceMac)
            
        print(addFlow)
    cur.close()
    conn.close()
    
InsertToMysql()