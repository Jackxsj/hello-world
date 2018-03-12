# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 16:31:32 2017

@author: Administrator
"""

import mysql.connector
import datetime
import xlwings as xw
import os,sys
import pandas as pd

class sqlToexcel:
    def export(self,field_name,res_all):
        #设置这个工作薄
        wbk = xw.Book('111.xlsx')
        #设置这个sheet,所有的操作，都是在sheet上进行的
        sht = wbk.sheets['Sheet1']
        #default_style = self.set_style('Times New Roman',220,False)
        
        df = pd.DataFrame(res_all, columns=field_name)
        sht.range('A1').value = df
        sht.range('A1').options(pd.DataFrame, expand='table').value
        
        #df = pd.DataFrame([[1,2], [3,4]], columns=['a', 'b'])
        #sht.range('A1').value = df
        #sht.range('A1').options(pd.DataFrame, expand='table').value
        
        
        
    def __init__(self):
        print("begin")
        self.conn = mysql.connector.connect(
                host='30.254.180.201',
                user = 'wasu_test',
                passwd = 'My5q18o8',
                port = 3306,
                database='radius',
                charset='utf8')
    def close_sql_connect(self):
        self.conn.close()
        
    def init_sql(self):
        cur = self.conn.cursor()
        return cur
    def end_sql(self,cur):
        cur.close()
        
    def query(self,sql_input):
        cur = self.init_sql()
        #后期再加名字
        sek = "当前在线用户"
        now = datetime.datetime.now()
        sek_now = sek+str(now.year)+"-"+str(now.month)+"-"+str(now.day)+"-"+str(now.hour)+"-"+str(now.minute);
        try:
            time_moment = datetime.date(2018, 1, 1)
            print(time_moment)
            sql_query=sql_input
            cur.execute(sql_query,(time_moment))
            #num_fields = len(cur.description)
            field_name = [i[0] for i in cur.description]
            res_all = cur.fetchall()
            self.export(field_name,res_all)
                
        except mysql.connector.Error as e:
            print('query error!{}'.format(e))
        finally:
            self.end_sql(cur)     
     
s1 = "select * from jf_online_users where acctstoptime > \"%s\";"
s2 = "select * from jf_online_users where acctstoptime > \"%s\";"
a = sqlToexcel()
a.query(s1)
a.close_sql_connect()