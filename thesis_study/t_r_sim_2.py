# -*- coding: utf-8 -*-
from __future__ import division
import random
import numpy as np
import matplotlib.pyplot as plt
#测试t(r)
#测试输入数据
yta = 3183.73679109
beta =  2.74858658356

t=0
last_t =[[]*4 for i in range(0,11)]
for i in range(0,11):
    last_t[i].append(i+1)
    tmp_val = random.uniform(0,1)
    last_t[i].append(tmp_val)
    t1 = yta*((np.log(1/(1-tmp_val)))**(1/beta))
    last_t[i].append(t1)
    if i==0:
        last_t[i].append(t1)
    else:
        last_t[i].append(last_t[i-1][3]+t1)

for j in last_t:
    print str(j[0])+'<---->'+str(j[1])+'<---->'+str(j[2])+'<---->'+str(j[3])

total_y = 15
year_repair = [0 for i in range(0,total_y)]
print year_repair
cmp_year = [i*8760 for i in range(1,total_y+1)]
for i in range(0,10000):
    t=0
    while t<cmp_year[-1]:
        tmp_val = random.uniform(0,1)
        t1 = yta*((np.log(1/(1-tmp_val)))**(1/beta))
        t = t + t1
        
        for j in range(0,total_y):
            if t < cmp_year[j]:
                year_repair[j] = year_repair[j] + 1
                break;
print year_repair
#一年的时间会覆盖所有的故障点，所以故障会发生几次
    

ra = [[755555,80000,0.0291,69840,698.4,906093]]
ra.append([755555,80000,0.0379,90960,909.6,927425])
ra.append([755555,80000,0.0343,82320,823.2,918698])
#修复费用×发生概率=所花费的费用
#这里参考的是‘电力管理设备的费用’
#在参考文献中计算的那个维护费用是 0.1 × 24 ，产生的损失是10×24
#维修时间是 1day 计算
print ra[0][5]
print ra[0][0]+ra[0][1]+ra[0][3]+ra[0][4]
print ra[0][4]/ra[0][2]
print ra[0][3]/ra[0][2]
print '----'
print ra[1][4]/ra[1][2]
print ra[1][3]/ra[1][2]
print '----'
print ra[2][4]/ra[2][2]
print ra[2][3]/ra[2][2]

