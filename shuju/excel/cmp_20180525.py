# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 16:05:35 2017

@author: Administrator
"""

# -*- coding: utf-8 -*-
import xlwt
import xlrd



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
        cmp1 = "cmp1.xlsx"
        cmp2 = "cmp2.xlsx"

        
        data1 = xlrd.open_workbook(cmp1,on_demand=True)
        table = data1.sheets()[0]
        num_rows = table.nrows
        cmp1 = []
        for i in range(0,num_rows):
            cmp1.append("\'"+str(table.row(i)[0].value)[0:11]+"\'")
        print("total_list len is:")
        print(len(cmp1))
        print(cmp1)
        print("-------------------")
        
        data2 = xlrd.open_workbook(cmp2,on_demand=True)
        table2 = data2.sheets()[0]
        num_rows2 = table2.nrows
        cmp2 = []
        for i in range(0,num_rows2):
            cmp2.append("\'"+str(table2.row(i)[0].value)[0:11]+"\'")
        print("total_list len is:")
        print(len(cmp2))
        print(cmp2)
        print("-------------------")
        
        
        diff_b = []
        for j in cmp1:
            if j not in cmp2:
                diff_b.append(j)
                
                
        for i in diff_b:
            print(i,end=',')
        
                    

    def __init__(self):
        print("hello world")
        self.export()
        

a = readExcelAndCmp();
'''
n = 18268797100.0
s = "\'"+str(n)[0:11]+"\'"
print(s)
'''