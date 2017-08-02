# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 16:05:35 2017

@author: Administrator
"""

# -*- coding: utf-8 -*-
import xlwt
import xlrd
import random
import numpy as np 
import matplotlib.pyplot as plt
import re
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False

class readExcelAndPlot:
    #参考下面的连接
    #http://www.cnblogs.com/jiangzhaowei/p/5856617.html
    def set_style(self,name,height,bold=False): 
      style = xlwt.XFStyle() # 初始化样式 
      font = xlwt.Font() # 为样式创建字体 
      font.name = name # 'Times New Roman' 
      font.bold = bold 
      font.color_index = 4
      font.height = height
      style.font = font 
      # style.borders = borders 
      return style
    
    def export(self):
        r = "daily-report-"
        excel_name = []
        for i in range(0,4):
            s = r+str(i+1)+".xls"
            excel_name.append(s)
            
        date_val = []
        data_val = []
        date_real_val=[]
        people_val = []
        avg_req_val = []
        j=1
        for n in excel_name:   
            data = xlrd.open_workbook(n)
            table = data.sheets()[10]
            num_cols = table.ncols
            
            for i in range(6,num_cols):
                date_val.append(j)
                j = j+1
                date_real_val.append(table.row(1)[i].value)
                data_val.append(float(re.sub('%','0',table.row(31)[i].value)))
                t1 = float(table.row(5)[i].value)
                t2 = float(table.row(6)[i].value)
                people_val.append(t2/50)
                if t2 == 0:
                    t2 = 1
                avg_req_val.append(t1*10/t2)
            
        
        plt.plot(date_val,data_val, label=u'认证成功率')
        plt.plot(date_val,avg_req_val,label=u'认证平均请求次数*10')
        plt.plot(date_val,people_val,label=u'认证人数/50')
        plt.xticks(date_val, date_real_val, rotation=90)
        plt.legend(loc='upper left')
        plt.grid(True)
        plt.show()

    def __init__(self):
        print("hello world")
        self.export()
        

a = readExcelAndPlot();