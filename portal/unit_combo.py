# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 11:36:27 2018

@author: Administrator
"""

ip = "29.194.67.89"

ip_split = ip.split(".")
val = ""
for i in ip_split:
    if int(i)<16:
        val = val +"0" +str(hex(int(i))).lstrip("0x")+":"
    else:
        val = val +str(hex(int(i))).lstrip("0x")+":"


print(val.rstrip(":"))