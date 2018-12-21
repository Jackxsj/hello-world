# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 15:59:53 2018

@author: Administrator
"""
import mysql.connector
import numpy as np
import time
import struct

def getVal(tmp_k):
    return {
            '0':0,
            '1':1,
            '2':2,
            '3':3,
            '4':4,
            '5':5,
            '6':6,
            '7':7,
            '8':8,
            '9':9,
            'a':10,
            'b':11,
            'c':12,
            'd':13,
            'e':14,
            'f':15
            }.get(tmp_k)

def get2CharacterHex(tmp_s):
    return getVal(tmp_s[0])*16+getVal(tmp_s[1])

def readFromMysql():
    
    conn = mysql.connector.connect(user="jfwx", password="jiANfEi_wxm2015", 
                                   host="192.168.1.5", database="db_user")
    
    conn2 = mysql.connector.connect(user="jfwx", password="jfwxS@@5", 
                                   host="192.168.1.54", database="db_user")
    
    
    
    
    cur = conn.cursor()
    cur2 = conn2.cursor()
    cur.execute("select * from jf_old_user where id >000012 and id <00012000")
    
    
    
    for i in cur:
        valueCon= {}
        valueCon["id"] = "Default";
        valueCon["usermac"] = i[1];
        valueCon["username"] = i[2];
        valueCon["business_id"] = 1115;
        valueCon["created_at"] = str(i[3]);
        valueCon["valid_at"] = str(i[4]);
        valueCon["source"] = 4;
        
        insertONE = """
            insert into jf_old_user values (
                    %(id)s,
                    \"%(usermac)s\",
                    \"%(username)s\",
                    %(business_id)d,
                    \"%(created_at)s\",
                    \"%(valid_at)s\",
                    %(source)d)
        """%valueCon
        
        
        cur2.execute(insertONE)
        cur2.execute("Commit;")
        conn2.commit()

    cur.close()
    cur2.close()
    print("done and close")
    
readFromMysql()