# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 13:27:28 2018

@author: Administrator
"""
import datetime
import random

file_path="sql_out.txt"

f = open(file_path, "w")
d = datetime.datetime(2019, 10, 21, 0, 0, 0, 0)

id1 = 13383
id2 = 13383+300


for k in range(0,438):
    for j in range(0,6):
        for i in range(0,60,10):
            ss = d
            sql_s = '''UPDATE db_user.`jf_old_user` SET valid_at='%s' WHERE id>= %d and id < %d;'''%(ss,id1,id2)
            
            f.write(sql_s)
            f.write('\n')
            d = d + datetime.timedelta(minutes=10)
            id1 = id1+300
            id2 = id2+300
            
        d = d - datetime.timedelta(minutes=60)
        d = d + datetime.timedelta(hours=1)
    d = d - datetime.timedelta(hours=6)
    d = d +datetime.timedelta(days=1)
    f.write('\n')
    f.write('\n')
    f.write('\n')

            
f.close()

