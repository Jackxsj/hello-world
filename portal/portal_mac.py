#coding=utf-8
#TCP服务器端程序
import socket
import time
from ctypes import c_uint32
import hashlib
import socketserver

#仅在生成的时候用，生成的data.txt需要提供给jemeter使用

def readFromFile():
    file_path="data2.txt"
    f=open(file_path, "r")
    arpTable = {}
    x = 2 
    for i in f.readlines():
        tmp = i.split(',')
        
        tmp_req_id = [int(int(tmp[2])/256),int(tmp[2])%256]
        
        tmp_challenge = tmp[3].split(".")
        arpTable[tmp[1]]=[tmp[0],tmp_req_id,[int(xval) for xval in tmp_challenge],0]
        x = x+1
        if x > 800000:
            break;
    print("read all data in, and ready")
    return arpTable


arpTable = readFromFile()


HOST = '192.168.1.8'
PORT = 50100

HOST_int = [int(i) for i in HOST.split(".")]
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    

for i in arpTable:
    print(i)
    req_mac = bytearray() 
    #version
    req_mac.append(33)
    #macbind request
    req_mac.append(48)
    #chap
    req_mac.append(0)
    #RSV
    req_mac.append(0)
    #serial no
    req_mac.extend(arpTable[i][2][14:])
    #req_id
    req_mac.append(0)
    req_mac.append(0)
    #usr_ip
    req_mac.extend(arpTable[i][2][12:])
    #usr port
    req_mac.append(0)
    req_mac.append(0)
    #error code
    req_mac.append(0)
    #attr num
    req_mac.append(2)
    
    #user_mac
    req_mac.append(11)
    req_mac.append(8)
    req_mac.extend(arpTable[i][2][0:6])
    
    #acip
    req_mac.append(10)
    req_mac.append(6)
    req_mac.extend(HOST_int)
    
    s.sendto(req_mac,("192.168.1.8",2000))
    time.sleep(0.2)
    


            
        




