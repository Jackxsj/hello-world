# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 13:27:28 2018

@author: Administrator
"""
import time
import random

mac_x = {}
mac_x[1] ="abcdefgh"
t1 = time.time()
print(t1)
a = str(int(time.time()))+mac_x[1]
t2 = time.time()
print(t2)
print("-----------------")
t1 = time.time()
print(t1)
a = str(random.randint(1,110))+mac_x[1]
t2 = time.time()
print(t2)
