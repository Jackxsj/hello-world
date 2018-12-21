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
    
    file_path="portal_name.csv"
    f=open(file_path, "r",encoding='UTF-8')
        
    x = f.readlines()

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