# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 15:59:53 2018
这个是另外一个盒子作为CDN的情况

Box1 ----Box2
|
User1(zll)  User2(zll)

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
    
    timeRange = pd.date_range('2018-11-09 10:00:36', '2019-01-29 11:30:00', freq= '20min')
    
    
    
    d1000 = {}
    d1000["37353925-6BE22460-4B26CA00-zll"] = "02:81:28:f8:d7:01"
    d1000["37353925-6BE22460-4B26CA00-zll2"] = "02:81:28:f8:d7:02"
    
    d2000 = {}
    d2000["1000000"] = ["1000001"]

    
    dev_map = {}
    dev_map["1000000"] = "68:f7:28:f8:dc:3c"
    dev_map["1000004"] = "02:81:28:f8:c7:d7"
    dev_map["1000005"] = "02:81:28:f8:c7:d8"
    dev_map["1000013"] = "02:81:f6:cf:1c:f2"
    dev_map["1000014"] = "02:81:5d:ab:98:14"
    
    maindev = "1000013"
    bakdev = "1000014"
    
    usr1 = "37353925-6BE22460-4B26CA00-zll"
    usr2 = "37353925-6BE22460-4B26CA00-zll2"
    
    onePack = 100000000000;
    
    for i in timeRange:
        if onePack < 0:
            TotalData = 0
            cur.close()
            conn.close()
            return
        else:
            TotalData = random.randint(0,200000)
            if (onePack - TotalData) > 0:
                onePack = onePack - TotalData
            else:
                TotalData = onePack
                onePack = -1      
        DateTime = str(i)
    
        
        tmpVal = random.randint(0,1)
        if tmpVal == 0:
            #盒子1000004上报
            SourceCategory = 1000
            DesCategory = 1200
            SourceID = maindev
            DestID = usr1
            DestMac = d1000[DestID]
            SourceMac = dev_map[SourceID]
            addFlow = sqlGe(SourceCategory,DesCategory,SourceID,DestID,TotalData,DateTime,DestMac,SourceMac)
            cur.execute(addFlow)
            cur.execute("Commit;")
            conn.commit()        
            
            
        else:
            SourceCategory = 1000
            DesCategory = 1000
            SourceID = bakdev
            DestID = maindev
            DestMac = dev_map[DestID]
            SourceMac = dev_map[SourceID]
            addFlow = sqlGe(SourceCategory,DesCategory,SourceID,DestID,TotalData,DateTime,DestMac,SourceMac)
            cur.execute(addFlow)
            cur.execute("Commit;")
            conn.commit()
            
            SourceCategory = 1000
            DesCategory = 1200
            SourceID = maindev
            DestID = usr1
            DestMac = d1000[DestID]
            SourceMac = dev_map[SourceID]
            addFlow = sqlGe(SourceCategory,DesCategory,SourceID,DestID,TotalData,DateTime,DestMac,SourceMac)
            cur.execute(addFlow)
            cur.execute("Commit;")
            conn.commit()
            
        tmpUser = random.randint(0,1)
        if tmpUser == 0:
            SourceCategory = 1000
            DesCategory = 1200
            SourceID = maindev
            DestID = usr2
            DestMac = d1000[DestID]
            SourceMac = dev_map[SourceID]
            addFlow = sqlGe(SourceCategory,DesCategory,SourceID,DestID,TotalData,DateTime,DestMac,SourceMac)
            cur.execute(addFlow)
            cur.execute("Commit;")
            conn.commit()
            
    cur.close()
    conn.close()
    
InsertToMysql()