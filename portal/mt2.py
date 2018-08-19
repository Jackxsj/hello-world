# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 10:44:55 2018

@author: Administrator
"""
import multiprocessing
import threading

import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('192.168.1.8',9080))
s.listen(5)

def action(conn):
    while True:
        data=conn.recv(1024)
        print(data)
        conn.send(data.upper())

if __name__ == '__main__':

    while True:
        conn,addr=s.accept()


        p=threading.Thread(target=action,args=(conn,))
        p.start()