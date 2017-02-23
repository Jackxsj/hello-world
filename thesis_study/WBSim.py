# -*- coding: utf-8 -*-
from __future__ import division
import random
import numpy as np
import matplotlib.pyplot as plt
#测试最简单的威布尔模型，看下威布尔曲线是什么样子的
def f_s(t,beta,yta,gama):
    tmp_v = (t-gama)/yta
    return (beta/yta)*((tmp_v)**(beta-1))*np.exp(-(tmp_v)**beta)
    
    

def M_C(num):
    count = 0
    for i in range(1,num+1):
        x = random.uniform(0,1)
        y = random.uniform(0,1)
        if x**2+y**2<1 :
            count+=1
    return 4.0*count/num


t = np.linspace(0, 4, 1000)
beta = 3.25
yta = 1
gama = 0
F = []
for tt in t:
    F.append(f_s(tt,beta,yta,gama))

plt.plot(t, F)
plt.show()

