# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 10:47:29 2018

@author: Administrator
"""

import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('192.168.1.8',9080))

while True:
    msg=input('>>: ').strip()
    if not msg:continue

    s.send(msg.encode('utf-8'))
    data=s.recv(1024)
    print(data)