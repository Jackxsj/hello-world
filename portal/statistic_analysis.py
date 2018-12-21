# -*- coding: utf-8 -*-
"""
checking analysis data
"""
import mysql.connector
import numpy as np
import time
import struct
import pandas as pd
import random


def SelectFromMysql():

    db_statistic_conn = mysql.connector.connect(user="jfwx", password="jfwxS@@5", 
                                   host="192.168.1.54", database="db_statistic")    
    db_statistic_cur = db_statistic_conn.cursor()
    
    group_id_0 = 1169
    group_id_1 = 1170
    group_id_2 = 1171
    group_id_3 = 1172
    
    date = "20181115"
    date_f = date[0:4]+"-"+date[4:6]+"-"+date[6:]
    hour = "15"
    
    cx1 = """SELECT count(mac) FROM new_user WHERE group_id_0 = 1169 and reg_time like "%s%%";""" %date_f
    #cx1 = """SELECT * FROM new_user WHERE group_id_0 = 1169 and reg_time like "%s%%";""" %date_f
    print(cx1)
    db_statistic_cur.execute(cx1)
    for i in db_statistic_cur:
        print(i[0])

    
SelectFromMysql()