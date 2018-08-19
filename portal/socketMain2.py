#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 22:14:58 2018

@author: jack
"""
from socket import *
import socketserver

import time


def getAllValue():
    allVal = {}
    for i in range(1,256):
        tmpVal = bytearray()
        tmpVal.append(i)
        tmpVal.extend(b"WithResponseAdded")
        allVal[i] = tmpVal
    
    for i in range(256,1000000):
        allVal[i] = "Non senseble value........."
    return allVal

            
class MyUDPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request[0]
        socket = self.request[1]
        tmp_address = self.client_address
        token = int(self.data[0])
        print("received token : "+str(token))
        if token <= 255 and token >= 1: 
            if token % 2 == 1:
                socket.sendto(allVal[token],tmp_address)
            elif token % 2 == 0:
                socket.sendto(allVal[token],tmp_address)
                
if __name__ == "__main__":
    HOST = '192.168.3.17'
    PORT = 2000
    allVal = getAllValue()
    s = socketserver.ThreadingUDPServer((HOST,PORT),MyUDPHandler)
    s.serve_forever()