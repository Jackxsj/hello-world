#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 23:21:04 2017

@author: jack
"""
import numpy as np

import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False

a_c = 0.01512

N_one = 0.5+0.75+1.5+0.75+1


def get_value(m):
    N_g_multi = N_one*m
    U = (1+a_c*((N_g_multi-1)**0.49))/((N_g_multi)**0.5)
    Q_g = 0.2*U*N_g_multi
    return Q_g

plt.figure(1)

x = np.linspace(1, 2000, 100)
y = []
for i in x:
    y.append(get_value(i))
plt.figure(1)  

cof = np.polyfit(x,y,3) 
p=np.poly1d(cof) 
print cof
print p

#x**a+b to sim
def fund(x, a, b):  
    return (x**a)*b

popt, pcov = curve_fit(fund, x, y)
y2 = [fund(i, popt[0],popt[1]) for i in x] 
print 'the value caculated:'
print popt
plt.plot(x,y,label=u'设计秒流量(L/s)')
plt.plot(x,y2,'--',label=u'设计秒流量回归曲线(L/s)')
plt.legend(loc='upper left')
plt.xlabel(u'户数')
plt.ylabel(u'流量(L/s)')
plt.show()
