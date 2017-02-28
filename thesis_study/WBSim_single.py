# -*- coding: utf-8 -*-
from __future__ import division
import random
import numpy as np
import matplotlib.pyplot as plt
#带入不同的参数看下威布尔分布和累积失效概率，需要给all_val赋值
ceshi_gao_wei_shui_xiang_1_tmp = [1.91938132137,2718.20937555,8760]
ceshi_gao_wei_shui_xiang_from_paper = [2.608,2.202,1]
#给all_val 赋值
all_val = ceshi_gao_wei_shui_xiang_from_paper


def f_s(t,beta,yta,gama):
    tmp_v = (t-gama)/yta
    return (beta/yta)*((tmp_v)**(beta-1))*np.exp(-(tmp_v)**beta)
    
def F_sum(t,beta,yta,gama):
    return 1-np.exp(-((t-gama)/yta)**beta)

plt.figure(1)
beta =  all_val[0]
yta = all_val[1]
#当值较大时，根据传入的参数来判断是用小还是大
if all_val[2] > 1000:
    threshold = all_val[2]
else:
    threshold = 10
gama = 0
t = np.linspace(0, threshold, 100)
Fa = []
Fb = []
for tt in t:
    Fa.append(f_s(tt,beta,yta,gama))
    Fb.append(F_sum(tt,beta,yta,gama))
plt.subplot(121)
plt.xlabel(u'Fs')
plt.plot(t, Fa)

plt.subplot(122)
plt.xlabel(u'F_sum')
plt.plot(t, Fb)

plt.show()

