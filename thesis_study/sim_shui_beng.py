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

def get_sheet_with_name(by_name,Q,H,P):
    data = open_excel()
    table = data.sheet_by_name(by_name)
    Q_value = table.row_values(1)
    for j in range(1, len(Q_value)):
        Q.append(Q_value[j])
        
    H_value = table.row_values(2)
    for j in range(1, len(H_value)):
        H.append(H_value[j])
        
    P_value = table.row_values(3)
    for j in range(1, len(P_value)):
        P.append(P_value[j])
    
            
Q40 = []
H40 = []
P40 = []
get_sheet_with_name(u'beng_40D',Q40,H40,P40)
print Q40
print H40
print P40

Q50 = []
H50 = []
P50 = []
get_sheet_with_name(u'beng_50D',Q50,H50,P50)
print Q50
print H50
print P50

Q80 = []
H80 = []
P80 = []
get_sheet_with_name(u'beng_80D',Q80,H80,P80)
print Q80
print H80
print P80

Q100 = []
H100 = []
P100 = []
get_sheet_with_name(u'beng_100D',Q100,H100,P100)
print Q100
print H100
print P100

Q150 = []
H150 = []
P150 = []
get_sheet_with_name(u'beng_150D',Q150,H150,P150)
print Q150
print H150
print P150

def fund40(x, a, b, c, d):  
    return x*a*((Q40[0])**b)+c*Q40[0]+d
popt, pcov = curve_fit(fund40, H40, P40)
P40_est = [fund40(i,popt[0],popt[1],popt[2],popt[3]) for i in H40] 
print 'the value caculated 40 :'
print popt
plt.scatter(H40,P40,label=u'40DL6.2-12*n')
plt.plot(H40,P40_est,'--',label=u'拟合40DL6.2-12*n')
plt.legend(loc='upper left')

def fund50(x, a, b, c, d):  
    return x*a*((Q50[0])**b)+c*Q50[0]+d
popt, pcov = curve_fit(fund50, H50, P50)
P50_est = [fund50(i,popt[0],popt[1],popt[2],popt[3]) for i in H50] 
print 'the value caculated popt 50:'
print popt
plt.scatter(H50,P50,label=u'50DL12.6-12.5*n')
plt.plot(H50,P50_est,'--',label=u'拟合50DL12.6-12.5*n')
plt.legend(loc='upper left')

def fund80(x, a, b, c, d):  
    return x*a*((Q80[0])**b)+c*Q80[0]+d
popt, pcov = curve_fit(fund80, H80, P80)
P80_est = [fund80(i,popt[0],popt[1],popt[2],popt[3]) for i in H80] 
print 'the value caculated popt 80:'
print popt
plt.scatter(H80,P80,label=u'80DL50.4-20*n')
plt.plot(H80,P80_est,'--',label=u'拟合80DL50.4-20*n')
plt.legend(loc='upper left')

def fund100(x, a, b, c, d):  
    return x*a*((Q100[0])**b)+c*Q100[0]+d
popt, pcov = curve_fit(fund100, H100, P100)
P100_est = [fund100(i,popt[0],popt[1],popt[2],popt[3]) for i in H100] 
print 'the value caculated popt 100:'
print popt
plt.scatter(H100,P100,label=u'100DL100-20*n')
plt.plot(H100,P100_est,'--',label=u'拟合100DL100-20*n')
plt.legend(loc='upper left')

def fund150(x, a, b, c, d):  
    return x*a*((Q150[0])**b)+c*Q150[0]+d
popt, pcov = curve_fit(fund150, H150, P150)
P150_est = [fund150(i,popt[0],popt[1],popt[2],popt[3]) for i in H150] 
print 'the value caculated popt 150:'
print popt
plt.scatter(H150,P150,label=u'150DL150-20*n')
plt.plot(H150,P150_est,'--',label=u'拟合150DL150-20*n')
plt.legend(loc='upper left')
plt.xlabel(u'扬程（米）')
plt.ylabel(u'价格（元/台）')
plt.show()

Q_all = []
Q_all.extend(Q40)
Q_all.extend(Q50)
Q_all.extend(Q80)
Q_all.extend(Q100)
Q_all.extend(Q150)
Q_tmp = [Q40[0],Q50[0],Q80[0],Q100[0],Q150[0]]

H_all = []
H_all.extend(H40)
H_all.extend(H50)
H_all.extend(H80)
H_all.extend(H100)
H_all.extend(H150)
H_tmp = [H40,H50,H80,H100,H150]

P_all = []
P_all.extend(P40)
P_all.extend(P50)
P_all.extend(P80)
P_all.extend(P100)
P_all.extend(P150)

print Q_all
print len(Q_all)
print H_all
print len(H_all)
print P_all
print len(P_all)


def fund_all(h_q,a,b,c,d):
    return h_q[0]*a*((h_q[1])**b)+c*h_q[1]+d

plt.figure(2)
x = scipy.array([H_all,Q_all])
print x
y = scipy.array(P_all)
print y

popt_all, pcov_all = curve_fit(fund_all, x, y)
print 'the value caculated popt 150:'
print popt_all
for ii in range(0,len(Q_tmp)):
    y_est = [fund_all([i,Q_tmp[ii]],popt_all[0],popt_all[1],popt_all[2],popt_all[3]) for i in H_tmp[ii]]
    plt.plot(H_tmp[ii],y_est,'--',label=u'regression')
    

plt.scatter(H_all,y,label=u'all_points')
plt.legend(loc='upper left')
plt.xlabel(u'扬程（米）')
plt.ylabel(u'价格（元/台）')
plt.show()

fig = plt.figure()
ax = fig.add_subplot(121, projection='3d')
ax.set_xlabel(u'流量（m^3/h）')
ax.set_ylabel(u'扬程（米）')
ax.set_zlabel(u'价格（元/台）')
ax.scatter(Q_all, H_all, P_all, s=50)

Q_all.sort()
qmin=min(Q_all)
qmax=max(Q_all)
H_all.sort()
hmin = min(H_all)
hmax = max(H_all)
print '------test here'
print Q_all
print P_all
X0 = np.arange(qmin, qmax, 5)
Y0 = np.arange(hmin, hmax, 5)
print '----checking here----'
print X0
print Y0
X,Y = np.meshgrid(X0,Y0)
print X
print Y

def fun_z(x,y):
    return x*popt_all[0]*(y**popt_all[1])+popt_all[2]*y+popt_all[3]
zs = np.array([fun_z(x1,y1) for x1,y1 in zip(np.ravel(X), np.ravel(Y))])
print len(zs)
Z = zs.reshape(X.shape)


ax = fig.add_subplot(122, projection='3d')
ax.set_xlabel(u'流量（m^3/h）')
ax.set_ylabel(u'扬程（米）')
ax.set_zlabel(u'价格（元/台）')
ax.plot_surface(X, Y, Z)
plt.show()