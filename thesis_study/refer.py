#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 10:04:14 2017

@author: jack
"""
import numpy as np

import matplotlib.pyplot as plt

dat = []
dat.append(1138)
dat.append(1209)
dat.append(1288)
dat.append(1362)
dat.append(1483)
dat.append(1602)
dat.append(1723)
dat.append(1865)
dat.append(2038)
dat.append(2176)
dat.append(2329)
dat.append(2398)
dat.append(2512)
dat.append(2638)
dat.append(2760)
dat.append(2906)
dat.append(3155)
dat.append(3270)
dat.append(3319)
dat.append(3448)
dat.append(3521)
dat.append(3608)
dat.append(3682)
dat.append(3823)
dat.append(3965)
dat.append(4080)
dat.append(4163)
dat.append(4295)
dat.append(4371)
dat.append(4520)

plt.figure(1)
x = [i for i in range(1,31)]

plt.plot(x,dat)
    
#test with select sequence, should begin with real number such as 1
#sel_n = [1,4,6,10,11,13,16,18,20,23,25,27,30]
sel_n = [n for n in range(1,31)]

y = [(j-1) for j in range(1,len(sel_n)+1)]
sel_data = [dat[(k-1)] for k in sel_n]
A_exp = []
for l in y:
    if l==0:
        A_exp.append(1)
    else:
        m = A_exp[l-1]+(len(dat)+1-A_exp[l-1])/(len(dat)-sel_n[l]+2.0)
        A_exp.append(m)


Fnt = []
for n in y:
    Fnt.append((A_exp[n]-0.3)/(len(dat)+0.4))

x_t = [np.log(dat[h-1]) for h in sel_n]
print x_t
print x_t[0]
y_t = [np.log(np.log(1.0/(1-i))) for i in Fnt]
print y_t

plt.figure(2)
plt.scatter(x_t,y_t)

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


A_ = (avg_(mul_2(x_t,y_t))-x_*y_)/(avg_(mul_(x_t))-x_*x_)
print A_
B_ = y_-A_*x_
print B_

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
gama = 0

F = []
for tt in t:
    F.append(f_s(tt,beta,yta,gama))

plt.plot(t, F)
plt.show()
