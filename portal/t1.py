# -*- coding: utf-8 -*-
import xlwt
import xlrd
import datetime

pass_0 = 'Fail'
pass_1 = 'Pass'

class opExcel:
    #参考下面的连接
    #http://www.cnblogs.com/jiangzhaowei/p/5856617.html
    
    def set_style(self,name,height,colour=4,bold=False): 
      style = xlwt.XFStyle() # 初始化样式 
      font = xlwt.Font() # 为样式创建字体 
      font.name = name # 'Times New Roman' 
      font.bold = bold 
      font.colour_index = colour
      font.height = height
      style.font = font 
      # style.borders = borders 
      return style
    def importExcel(self):
        data = xlrd.open_workbook(self.fileName)
        sheet = data.sheets()[0]
        nrows = sheet.nrows
        values = []
        
        for i in range(1,nrows):
            tmpVal = sheet.row_values(i)
            values.append([tmpVal[0],tmpVal[1],tmpVal[2],tmpVal[3],tmpVal[4],[],[]])
        return values
    
    def exportExcel(self,dataOut):
         data = xlwt.Workbook()
         sheet = data.add_sheet(u'测试结果')
         print sheet.name
         default_style = self.set_style('Times New Roman',220,4,True)
         green = self.set_style('Times New Roman',220,3,False)
         red = self.set_style('Times New Roman',220,2,False)
         sheet.write(0,0,u'序号',default_style)
         sheet.write(0,1,u'测试URL',default_style)
         sheet.write(0,2,u'请求方法',default_style)
         sheet.write(0,3,u'参数',default_style)
         sheet.write(0,4,u'测试结果',default_style)
         sheet.write(0,5,u'响应',default_style)
         j=1
         for tmpData in dataOut:
             sheet.write(j,0,tmpData[0])
             sheet.write(j,1,tmpData[1])
             sheet.write(j,2,tmpData[2])
             sheet.write(j,3,tmpData[3])
             if tmpData[5]== pass_0 :
                 sheet.write(j,4,tmpData[5],red)
             else :
                 sheet.write(j,4,tmpData[5],green)
            
             sheet.write(j,5,tmpData[6])
             j=j+1
         nowTime=datetime.datetime.now().strftime('%Y%m%d%H%M%S')
         outFileName = u'测试结果'+nowTime+'.xls' 
         data.save(outFileName)



    def __init__(self,fileName=u'测试用例.xls'):
        self.fileName = fileName 
        
        
a=opExcel();
b=a.importExcel()
b[0][5]='Fail'
b[0][6]='response 200'
print b
a.exportExcel(b)
