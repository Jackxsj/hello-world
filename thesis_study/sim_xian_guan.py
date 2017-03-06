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
import xlrd
import scipy
from mpl_toolkits.mplot3d import Axes3D
mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False

#水泵流量
#Q40=[6.2, 6.2, 6.2, 6.2, 6.2, 6.2, 6.2, 6.2, 6.2, 6.2, 6.2]
#H40=[24,	36,	48,	60,	72,	84,	96,	108,	120,	132,	 144]
#P40=[2711,3211,3475,4031,4309,4935,5352,5908,6394,7020,8757]

def open_excel(file= '/home/jack/share/lunwen/data.xlsx'):
     try:
         data = xlrd.open_workbook(file)
         return data
     except Exception,e:
         print str(e)

def get_sheet_with_name(by_name,Q,H):
    data = open_excel()
    table = data.sheet_by_name(by_name)
    Q_value = table.row_values(1)
    for j in range(1, len(Q_value)):
        Q.append(Q_value[j])
        
    H_value = table.row_values(2)
    for j in range(1, len(H_value)):
        H.append(H_value[j])
        
   
    
            
D_val = []
P_val = []
get_sheet_with_name(u'xian_guan',D_val,P_val)
print D_val
print P_val



def fund(x, a, b):  
    return a*(x**b)
popt, pcov = curve_fit(fund, D_val, P_val)
P_est = [fund(i,popt[0],popt[1]) for i in D_val] 
print 'the value caculated 40 :'
print popt

plt.scatter(D_val,P_val,label=u'单价')
plt.plot(D_val,P_est,label=u'单价拟合曲线')
plt.legend(loc='upper left')
plt.xlabel(u'外径（mm）')
plt.ylabel(u'单价（元/m）')
plt.legend(loc='upper left')


plt.show()