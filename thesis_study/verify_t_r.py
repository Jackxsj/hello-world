# -*- coding: utf-8 -*-
from __future__ import division
import random
import numpy as np
import matplotlib.pyplot as plt
#验证电子设备管理中的周期分析

all_c = []

all_c.append([1,2145])
all_c.append([2,3145])
all_c.append([3,3453])
all_c.append([4,3649])
all_c.append([5,3760])
all_c.append([6,3673])
all_c.append([7,3667])
all_c.append([8,3583])
all_c.append([9,3754])
all_c.append([10,3678])
print all_c
t=0
for i in all_c:
    t = t+i[1]

print t