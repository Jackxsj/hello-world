#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 22:29:55 2017

@author: jack
"""

import matplotlib.pyplot as plt
import numpy as np
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False
t1 = []
t2 = []
t3 = []

tx = 10
ty = 0
x = [i for i in range(1,101)]
for i in range(1,30):
    tx = tx - 0.05*i
    t1.append(tx)
for i in range(30,50):
    tx = tx - 0.01*i
    t1.append(tx)
for i in range(50,70):
    tx = tx + 0.01*i
    t1.append(tx)
for i in range(70,101):
    tx = tx + 0.03*i
    t1.append(tx)  
    
plt.figure(1)
plt.plot(x,t1)


plt.figure(2)
def fx1(x):
    return (x-1)**2+0.5
def fx2(x):
    return (x-2)**2+0.5

time1 = np.linspace(0.2,1,5)
y1 = []
for i in time1:
    y1.append(fx1(i))
time2 = np.linspace(1,2,5)
y2 = []
for j in time2:
    y2.append(0.5)

time3 = np.linspace(2,2.8,5)
y3 = []
for j in time3:
    y3.append(fx2(j))
time4 = [1,1,1,1,1]
y4 = []
for j in range(0, len(time4)):
    y4.append(j*0.3)
time5 = [2,2,2,2,2]
y5 = []
for j in range(0, len(time5)):
    y5.append(j*0.3)
    
plt.plot(time1,y1,color='r')
plt.plot(time2,y2,color='r')
plt.plot(time3,y3,color='r')
plt.plot(time4,y4,'--', color='y')
plt.plot(time5,y5,'--',color='y')
plt.xlabel(u'时间')
plt.ylabel(u'故障率')
plt.text(0.5,0.2,u'早期',color='blue',ha='center')
plt.text(1.5,0.2,u'中期',color='blue',ha='center')
plt.text(2.5,0.2,u'后期',color='blue',ha='center')
plt.show()


