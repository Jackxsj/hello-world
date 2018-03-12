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

class readExcelAndCmp:
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
        total = "total.xls"
        online = "online.xls"
        excel_name = []
        excel_name.append(total)
        excel_name.append(online)
        
        data = xlrd.open_workbook(total,on_demand=True)
        table = data.sheets()[0]
        num_rows = table.nrows
        total_list = []
        for i in range(1,num_rows):
            tmp = []
            tmp.append(table.row(i)[0].value)
            tmp.append(table.row(i)[1].value)
            tmp.append(table.row(i)[2].value)
            total_list.append(tmp)
        print("total_list len is:")
        print(len(total_list))
        print(total_list)
        print("-------------------")
        data.release_resources()
        del data
           
        data_rows_online = xlrd.open_workbook(online)
        table_rows_online = data_rows_online.sheets()[0]
        num_rows_online = table_rows_online.nrows
        online_list = []
        for i in range(1,num_rows_online):
            online_list.append(table_rows_online.row(i)[0].value)
        
        diff_b = []
        for j in total_list:
            b = j[0].upper()
            if b not in online_list:
                diff_b.append(j)
        
                    
        default_style = self.set_style('Times New Roman',220,False)
        #设置这个工作薄
        wbk = xlwt.Workbook()
        #设置这个sheet,所有的操作，都是在sheet上进行的
        sheet1 = wbk.add_sheet('cmp_res',cell_overwrite_ok=True)
        row_j = 0
        for i in range(0,len(diff_b)): 
            sheet1.write(row_j,0,diff_b[i][0],default_style)
            sheet1.write(row_j,1,diff_b[i][1],default_style)
            sheet1.write(row_j,2,diff_b[i][2],default_style)
            row_j = row_j + 1
        #save
        wbk.save('cmp_res.xlsx')

    def __init__(self):
        print("hello world")
        self.export()
        

a = readExcelAndCmp();