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
                                   host="192.168.1.5", database="db_authentication")    
    db_statistic_cur = db_statistic_conn.cursor()
    
    file_path="trend_2018-11-19.csv"
    f=open(file_path, "r",encoding='UTF-8')
    
    today = datetime.date.today()                                                          # 今天
    yesterday = str(today - datetime.timedelta(days=1)) 
    
    x = f.readlines()
    for i in x:
        i_tmp = i.split()
        valueCon= {}
        valueCon["id"] = "Default"
        valueCon["group_id"] = int(i_tmp[0])
        valueCon["group_name"] = i_tmp[1]
        valueCon["auth_num"] = int(i_tmp[2])
        valueCon["auth_date"] = yesterday
        addFlow = """insert into auth_trend values (
         %(id)s,
         %(group_id)d,
         \"%(group_name)s\",
         %(auth_num)d,
         \"%(auth_date)s\"
         )"""%valueCon
        db_statistic_cur.execute(addFlow);
        db_statistic_cur.execute("Commit;")
    db_statistic_conn.commit() 
    db_statistic_conn.close()
    db_statistic_cur.close()
    
ReadFromFileAndInsertToMysql()