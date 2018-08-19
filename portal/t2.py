# -*- coding: utf-8 -*-
import xlwt
import xlrd
import datetime
import requests

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
    def exportTest(self):
        data = xlwt.Workbook()
        sheet = data.add_sheet(u'测试结果') 
        j=1
        
        for j in range(1,32):
            color = self.set_style('Times New Roman',220,j+1,False)
            sheet.write(j,0,j,color)
        outFileName = u'test.xls' 
        data.save(outFileName)
             
    def importExcel(self):
        data = xlrd.open_workbook(self.fileName)
        sheet = data.sheets()[0]
        nrows = sheet.nrows
        values = []
        
        for i in range(1,nrows):
            tmpVal = sheet.row_values(i)
            values.append([tmpVal[0],tmpVal[1],tmpVal[2],tmpVal[3],tmpVal[4],tmpVal[5],[],[]])
        return values
    
    def exportExcel(self,dataOut):
         data = xlwt.Workbook()
         default_style = self.set_style('Times New Roman',220,8,True)
         green = self.set_style('Times New Roman',220,3,False)
         red = self.set_style('Times New Roman',220,2,False)
         
         
         tmpSuccess=0
         tmpFail=0
         
         
         sheet = data.add_sheet(u'测试结果')         
         sheet.write(0,0,u'序号',default_style)
         sheet.write(0,1,u'用例',default_style)
         sheet.write(0,2,u'请求方法',default_style)
         sheet.write(0,3,u'测试URL',default_style)
         sheet.write(0,4,u'参数',default_style)
         sheet.write(0,5,u'测试结果',default_style)
         j=1
         for tmpData in dataOut:
             sheet.write(j,0,tmpData[0])
             sheet.write(j,1,tmpData[1])
             sheet.write(j,2,tmpData[2])
             sheet.write(j,3,tmpData[3])
             sheet.write(j,4,tmpData[4])
             if tmpData[6]== pass_0 :
                 sheet.write(j,5,tmpData[6],red)
                 tmpFail=tmpFail+1
             else :
                 sheet.write(j,5,tmpData[6],green)
                 tmpSuccess=tmpSuccess+1            
             j=j+1
        
         sheet_sum = data.add_sheet(u'测试汇总')
         sheet_sum.write(0,0,u'测试成功',default_style)
         sheet_sum.write(0,1,u'测试失败',default_style)
         sheet_sum.write(0,2,u'总测试用例数',default_style)
         sheet_sum.write(0,3,u'测试成功率',default_style)
         sheet_sum.write(1,0,tmpSuccess,default_style)
         sheet_sum.write(1,1,tmpFail,default_style)
         sheet_sum.write(1,2,tmpSuccess+tmpFail,default_style)
         tmpR = tmpSuccess*1.0/(tmpSuccess+tmpFail)
         if(tmpR>0.9):
             sheet_sum.write(1,3,str(round(tmpR*100,2))+'%',green)
         else:
             sheet_sum.write(1,3,str(round(tmpR*100,2))+'%',red)
         
         nowTime=datetime.datetime.now().strftime('%Y%m%d%H%M%S')
         outFileName = u'测试结果'+nowTime+'.xls' 
         data.save(outFileName)



    def __init__(self,fileName=u'测试用例.xls'):
        self.fileName = fileName 
      
def reqTest(values):
    url = ""
    
    if '' == values[4]:
        url = values[3]
    else:
        url = values[3]+"?"+values[4]
    
    headers = {"Content-Type":"application/json"}
    if "get" == values[2] :
        req = requests.get(url=url,headers=headers)
    else:
        req = requests.post(url=url,headers=headers)
        
    if req.status_code == 200:
        values[6]=pass_1
        values[7]=req.status_code
    else:
        values[6]=pass_0
        values[7]=req.status_code
            

a=opExcel();
a.exportTest();

