#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 10:04:14 2017

@author: jack
"""
import numpy as np

import matplotlib.pyplot as plt

dat = []
ex_dat = [1138,1209,1288,1362,1483,1602,1723,1865,2038,2176,2329,2398,2512,2638,2760,2906,3155,3270,3319,3448,3521,3608,3682,3823,3965,4080,4163,4295,4371,4520]
ex_dat.sort()
for i in ex_dat:
    dat.append(i)

dat_len = len(dat)

plt.figure(1)
x = [i for i in range(1,dat_len+1)]

plt.plot(x,dat)
    
#test with select sequence, should begin with real number such as 1
#sel_n = [1,4,6,10,11,13,16,18,20,23,25,27,30]
sel_n = [n for n in range(1,dat_len+1)]


y = [ j for j in range(0,len(sel_n))]
print y
A_exp = []
#按照改进的中位秩公式来计算对应的秩次
for l in y:
    if l==0:
        A_exp.append(1)
    else:
        m = A_exp[l-1]+(len(dat)+1-A_exp[l-1])/(len(dat)-sel_n[l]+2.0)
        A_exp.append(m)

#用经验公式来计算Fn(t)来找到对应的概率
Fnt = []
for n in y:
    Fnt.append((A_exp[n]-0.3)/(len(dat)+0.4))
#来计算对应的ln(t) ln(ln(1/(1-F)))用来拟合
x_t = [np.log(dat[h-1]) for h in sel_n]
print x_t
print x_t[0]
y_t = [np.log(np.log(1.0/(1-i))) for i in Fnt]
print y_t

plt.figure(2)
plt.scatter(x_t,y_t)

#计算这些列标的平均值
def avg_(z_):
    m = 0
    for n in z_:
        m = m+n
    return m/len(z_)
def mul_(z_):
    w_ = []
    for i in range(0,len(z_)):
        w_.append( z_[i]*z_[i])
    return w_
def mul_2(z_,v_):
    w_ = []
    if len(z_) != len(v_):
        print 'error len'
        return
    for i in range(0,len(z_)):
        w_.append(z_[i]*v_[i])
    return w_

x_ = avg_(x_t)
y_ = avg_(y_t)

#拟合对应的A和B值
A_ = (avg_(mul_2(x_t,y_t))-x_*y_)/(avg_(mul_(x_t))-x_*x_)
print A_
B_ = y_-A_*x_
print B_
#根据A和B值来计算这个曲线
tmp_v = np.linspace(np.floor(x_t[0]),np.ceil(x_t[len(x_t)-1]),10)
tmp_y = [A_*k+B_ for k in tmp_v]
plt.figure(2)
plt.plot(tmp_v,tmp_y)
plt.show()


def f_s(t,beta,yta,gama):
    tmp_v = (t-gama)/yta
    return (beta/yta)*((tmp_v)**(beta-1))*np.exp(-(tmp_v)**beta)

t = np.linspace(0, 8000, 50)
beta = A_
yta = np.exp(-(B_/A_))
print 'beta is: '+str(beta)
print 'yta is:'+str(yta)
gama = 0

F = []
for tt in t:
    F.append(f_s(tt,beta,yta,gama))

plt.plot(t, F)
plt.show()
