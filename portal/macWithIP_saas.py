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
    '''
    conn = mysql.connector.connect(user="jfwx", password="jiANfEi_wxm2015", 
                                   host="192.168.1.5", database="db_user")
    '''
    conn = mysql.connector.connect(user="jfwx", password="jfwxS@@5", 
                                   host="192.168.1.54", database="db_user")
    
    
    
    
    cur = conn.cursor()
    
    cur.execute("select * from jf_old_user where id >000700 and id <0001000 and business_id = 1115")
    
    file_path="data.txt"
    file_path2="data2.txt"
    f=open(file_path, "w")
    f2=open(file_path2,"w")
    
    tmp_con = 1
    for i in cur:
        #pack 打包数据
        tmp_a = struct.pack('>l',int(i[0]))
        tmp_ip = [10]
        tmp_ip.extend(tmp_a[1:4])
        
        tmp_ip_val = [str(j) for j in tmp_ip]
        tmp_mac_val = str(i[1]).split("-")
        if len(tmp_mac_val) < 6:
            continue
        
        line = i[1]+","+".".join(tmp_ip_val)
        f.write(line)
        f.write('\n')
            
        mac_val = []
        
        for j in range(0,6):
            tmp_x = int(tmp_mac_val[j],16)   
            mac_val.append(tmp_x)
            
        
        challenge_val = []
        challenge_val.extend(mac_val)
        challenge_val.extend(mac_val)
        challenge_val.extend(tmp_ip)
        tmp_challenge_val = [str(j) for j in challenge_val]
        challenge_str = ".".join(tmp_challenge_val)
        
        accounting_id = "0"
        
        line2 = line+","+str(i[0]%65536)+","+challenge_str+","+accounting_id
        f2.write(line2)
        f2.write('\n')
        
        
        tmp_con = tmp_con + 1
        if tmp_con > 200:
            break
        
    f.close()
    f2.close()

    cur.close()
    print("done and close")
    
readFromMysql()