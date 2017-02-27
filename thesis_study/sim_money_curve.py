#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 17:51:35 2017

@author: jack
"""

import matplotlib.pyplot as plt
import random
import matplotlib.font_manager as fm
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False
#myfont = fm.FontProperties(fname='/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc') 
            
#refer below 2 link for this issue:
#https://my.oschina.net/cppblog/blog/10300
#http://blog.csdn.net/dgatiger/article/details/50414549

T = 100.0
N_year = 101
x_t = [i for i in range (1,N_year)]
T_avg = []
T_m = []
T_t = []

l=0
point=[]
for i in x_t:
    l_tmp=0.05*i+random.uniform(0,1)/10
    T_avg.append(T/i)
    l=l_tmp+l
    T_m.append(l/i)
    j = (T/i)+(l/i)
    if i >1:
        if j>T_t[i-2]:    
            point.append([i-1,T_t[i-2]])
    T_t.append(j)
    

x_conf = [point[0][0],point[0][0],0]
y_conf = [0,point[0][1],point[0][1]]


plt.figure(1)
s="初始投资年平均"
s.decode('utf-8')
s.decode('gbk', "ignore")
s.decode('gbk', 'replace')

print s

plt.plot(x_t,T_avg,'--',label=u'初始投资年平均')
plt.plot(x_t,T_m,'-.',label=u'维护费用年平均')
plt.plot(x_t,T_t,'-',label=u'年平均成本')
plt.plot(x_conf,y_conf,'r:')
plt.legend(loc='upper left')
plt.xlabel(u'时间')
plt.ylabel(u'成本')


plt.title(u'LCC年均成本')
plt.show()



