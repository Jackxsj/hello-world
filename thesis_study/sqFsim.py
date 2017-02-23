# -*- coding: utf-8 -*-
from __future__ import division
import random
import numpy as np
import matplotlib.pyplot as plt
#测试平均秩次下的威布尔模型参数
sq = [422,890,987,975,1098,980,1420,954,1678,2174,2354,970,998,2425,890,2819,975,3310,9186,5058]
sq.sort()


def mid_sq(sq_num,len):
    return (sq_num-0.3)/(len+0.4)

Fn = [mid_sq(i,len(sq)) for i in range(1,(len(sq)+1))]
# x = ln(t)
x=[np.log(det) for det in sq]
# y = ln(ln(1/(1-F)))
y=[np.log(np.log(1/(1-det_F))) for det_F in Fn]

for i in range(0,(len(sq))):
    print str(sq[i])+"---->"+str(x[i])+"--->"+str(y[i])

plt.scatter(x,y)
plt.show()

