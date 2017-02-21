# -*- coding: utf-8 -*-
from __future__ import division
import random
import numpy as np
import matplotlib.pyplot as plt


def M_C(num):
    count = 0
    for i in range(1,num+1):
        x = random.uniform(0,1)
        y = random.uniform(0,1)
        if x**2+y**2<1 :
            count+=1
    return 4.0*count/num

print '-----10000------'
print M_C(10000)

print '-----30000------'
print M_C(30000)

print '-----40000------'
print M_C(40000)


x = np.linspace(0, 2, 1000)
y = x ** 2
plt.plot(x, y)
plt.fill_between(x, y, where=(y > 0), color='red', alpha=0.5)



N = 10000
print np.random.rand(10,2)

points=[]
#这个x需要乘以2来进行扩大，y需要乘以4来进行扩大
for xy in np.random.rand(N, 2):
    points.append([xy[0]*2, xy[1]*4])

    
plt.scatter([x[0] for x in points], [x[1] for x in points], s=5, c=np.random.rand(N), alpha=0.5)

count = 0
for xy in points:
    if xy[1] < xy[0] ** 2:
        count += 1
print((count / N) * (2.0 * 4.0))

plt.show()

