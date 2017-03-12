#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 10:04:14 2017

@author: jack
"""
import numpy as np

import matplotlib.pyplot as plt
import xlwt
import xlrd
#test with select sequence, should begin with real number such as 1
#案例中的求秩如果数据残缺可以用下面这种跳位方式计算

#这个区别于gao_wei_shui_xiang主要是去除一些数据
#ex_dat = [460,824,150,264,938,1248,543,1378,1726,558,1988,548,2045,546,542,2234,2628,537,1901,3498]
#sel_n = [3,10,11,12,13,14,16,17,18,19]

#变频泵的计算
#ex_dat = [422,890,987,975,1098,980,1420,954,1678,2174,2354,970,998,2425,890,2819,975,3310,9186,5058]
#sel_n = [1,9,11,12,13,14,15,16,17,18]

#混合计算
ex_dat = [460,824,938,1248,1378,1726,1988,2045,2234,2628,422,987,1098,1420,1678,2174,2354,2425,2819,3310]
#不需要从中选取，即所有数据有效
sel_n = [n for n in range(1,len(ex_dat)+1)]


ex_dat.sort()
ex_tmp = [[i+1, ex_dat[i]] for i in range(0, len(ex_dat))]
print ex_tmp
    

dat = []
for i in sel_n:
    dat.append(ex_dat[i-1])
dat_len = len(dat)

print 'dat is here: '
print dat


#计算在list中的下标
y_list = [ j for j in range(0,len(sel_n))]

A_exp = []
#按照改进的中位秩公式来计算对应的秩次
last_in = 0
for l in y_list:
    if l==0:
        A_exp.append(1)
    else:
        m = A_exp[l-1]+(len(ex_dat)+1-A_exp[l-1])/(len(ex_dat)-sel_n[l]+2.0)
        A_exp.append(m)
print 'A_exp value is :'
print A_exp

#用经验公式来计算Fn(t)来找到对应的概率
Fnt = []
for n in y_list:
    Fnt.append((A_exp[n]-0.3)/(len(ex_dat)+0.4))
print 'Fnt is here:'
print Fnt
#来计算对应的ln(t) ln(ln(1/(1-F)))用来拟合
x_t = [np.log(dat[h]) for h in y_list]
print 'x_t is: '
print x_t

y_t = [np.log(np.log(1.0/(1-i))) for i in Fnt]
print 'y_t is: '
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
print 'value A is:'
print A_

B_ = y_-A_*x_
print 'value B is:'
print B_
#根据A和B值来计算这个曲线
tmp_v = np.linspace(np.floor(x_t[0]),np.ceil(x_t[len(x_t)-1]),10)
tmp_y = [A_*k+B_ for k in tmp_v]

plt.plot(tmp_v,tmp_y)
plt.show()


def f_s(t,beta,yta,gama):
    tmp_v = (t-gama)/yta
    return (beta/yta)*((tmp_v)**(beta-1))*np.exp(-(tmp_v)**beta)
def F_sum(t,beta,yta,gama):
    return 1-np.exp(-((t-gama)/yta)**beta)

t = np.linspace(0, 8000, 50)
beta = A_
yta = np.exp(-(B_/A_))
print 'beta is: '+str(beta)
print 'yta is:'+str(yta)
gama = 0

F = []
for tt in t:
    F.append(F_sum(tt,beta,yta,gama))

plt.plot(t, F)
plt.show()

###########下面为输出到excel
def set_style(name,height,bold=False): 
  style = xlwt.XFStyle() # 初始化样式 
  font = xlwt.Font() # 为样式创建字体 
  font.name = name # 'Times New Roman' 
  font.bold = bold 
  font.color_index = 4
  font.height = height
  style.font = font 
  # style.borders = borders 
  return style

#设置这个工作薄
wbk = xlwt.Workbook()
#设置这个sheet,所有的操作，都是在sheet上进行的
sheet1 = wbk.add_sheet('test1',cell_overwrite_ok=True)

row_j=1
for ii in y_list:
    sheet1.write(row_j,0,ii+1,set_style('Arial',220,False))
    sheet1.write(row_j,1,dat[ii],set_style('Arial',220,False))
    sheet1.write(row_j,2,A_exp[ii],set_style('Arial',220,False))
    sheet1.write(row_j,3,Fnt[ii],set_style('Arial',220,False))
    sheet1.write(row_j,4,x_t[ii],set_style('Arial',220,False))
    sheet1.write(row_j,5,y_t[ii],set_style('Arial',220,False))
    row_j=row_j+1
sek = 'issue'
wbk.save('%s.xlsx' %sek)