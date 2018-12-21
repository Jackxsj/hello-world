# -*- coding: utf-8 -*-
"""
checking analysis data
"""
import mysql.connector
import numpy as np
import datetime
import struct
import pandas as pd
import random


def ReadFromFileAndInsertToMysql():

    db_statistic_conn = mysql.connector.connect(user="jfwx", password="jiANfEi_wxm2015", 
                                   host="192.168.1.5", database="db_audit")    
    db_statistic_cur = db_statistic_conn.cursor()
    
    d1_morning = datetime(2018, 10, 8,9)
    d2_morning = datetime(2018, 11, 30,9)
    
    allD_morning = pd.date_range(d1_morning,d2_morning, freq= 'BD')
    allTime = []
    for i in allD_morning:
        tmpTime =  pd.date_range(i, periods=13, freq= 'H')
        allTime.extend(tmpTime)

    for i in x:
        valueCon= {}
        valueCon["id"] = "Default"
        valueCon["portal_name"] = i
        addFlow = """insert into portal_name values (
         %(id)s,
         \"%(portal_name)s\"
         )"""%valueCon
        print(addFlow)
        
        db_statistic_cur.execute(addFlow);
        db_statistic_cur.execute("Commit;")
       
    db_statistic_conn.commit()  
    db_statistic_conn.close()
    db_statistic_cur.close()
    
ReadFromFileAndInsertToMysql()