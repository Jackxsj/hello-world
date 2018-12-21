#!/usr/bin/python
import os
print("hello")
f = open("ruijie_20181115.log",'r')
lines = f.readlines()

for i in lines:
        c = []
        c = i.split('|')
        c[1] = c[1].strip()
        print(c)
        #item = """curl -H "Content-Type:application/json" -X POST --data ' {"sn":"%s","apMac":"%s"}' http://192.168.1.5:8080/authentication/snApmacMap/create""" %(c[1],c[0])
        item = """curl -H "Content-Type:application/json" -X POST --data ' {"sn":"%s","apMac":"%s"}' http://30.254.180.187:8080/authentication/snApmacMap/create""" %(c[1],c[0])
        print(item)
        os.popen(item)
