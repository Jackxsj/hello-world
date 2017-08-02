# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 16:05:35 2017

@author: Administrator
"""

# -*- coding: utf-8 -*-
import xlwt
import xlrd
import random


class sqlToexcel:
    def lancome15_write_rows():
        #将字段写入到EXCEL新表的第一行
        L = ['Id', 'Amount of money', 'Purchase times']
        for ifs in range(len(L)):
             sheet.write(0,ifs,L[ifs])
        wbk.save('lancome15_result_8.9.csv')
        sql = "SELECT DISTINCT category FROM lancome15_order_online" 
        cursor.execute(sql)
        numrows = int(cursor.rowcount)
        L = []
        for i in range(numrows):
            g = cursor.fetchone()
            sheet.write(0,i+3,g[0])
            L.append(g[0])
        wbk.save('lancome15_result_8.9.csv')
        

    def lancome15_write_cols():
        sql = "SELECT DISTINCT uid FROM lancome15_order_online" 
        cursor.execute(sql)
        numrows = int(cursor.rowcount)
        sum = 0
        for i in range(numrows):
            g = cursor.fetchone()
            sum += 1
            sheet.write(i+1,0,g[0])
        wbk.save('lancome15_result_8.9.csv')


    def lancome15_read_excel():
        workbook = xlrd.open_workbook(r'E:\work\lancome15_result_8.9.csv')
        sheet1 = workbook.sheet_by_index(0) # sheet索引从0开始
        rows = sheet1.row_values(0) 
        cols = sheet1.col_values(0) 
        return rows[3::],cols[1::]

    def lancome15_result_func():
        result = lancome15_read_excel()
        row_name = result[0] 
        col_name = result[1] 
        for i in range(len(col_name)):
            sql1 = "SELECT SUM(ogn*price), COUNT(oid) FROM lancome15_order_online where uid = '%s'" % (col_name[i])
            cursor.execute(sql1)
            g = cursor.fetchone()           
            sheet.write(i+1,1,g[0])
            sheet.write(i+1,2,g[1])
            for j in range(len(row_name)): 
                sql2 = 'SELECT COUNT("%s") FROM lancome15_order_online where uid = "%s" AND category = "%s"' \
                  % (row_name[j], col_name[i], row_name[j]) 
                cursor.execute(sql2)
                f = cursor.fetchone() 
                sheet.write(i+1,j+3,f[0])
        wbk.save('lancome15_result_8.9.csv')

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
        sek = "box_traffic_hour"
        data = xlrd.open_workbook('device_mac.xls')
        table = data.sheets()[0]
        nrows = table.nrows
        device = []
        for i in range(nrows):
            device.append(table.row_values(i))
        print(device)
        field_names = ["device_mac","start_time","end_time","cdn_down_traffic",
                       "box_up_traffic","share_down_traffic"]
        print(len(device))
        
        #设置这个工作薄
        wbk = xlwt.Workbook()
        #设置这个sheet,所有的操作，都是在sheet上进行的
        sheet1 = wbk.add_sheet('box_traffic_hour',cell_overwrite_ok=True)
        for i in range(0,len(field_names)): 
            sheet1.write(0,i,field_names[i],self.set_style('Times New Roman',220,True))
        
        row_j = 1
        default_style = self.set_style('Times New Roman',220,False)
        ####生成6月份的数据
        for day in range(1,31):
            for h in range(1,25):
                for dev in range(0,1): 
                    sheet1.write(row_j,0,device[dev][0],default_style)
                    time_start = "2017/6/"+str(day)+" "+str(h-1)+":00:00"
                    sheet1.write(row_j,1,time_start,default_style)
                    time_end = ""
                    if h == 24:
                        if day == 30:
                            time_end = "2017/7/1"+" 0:00"
                        else:
                            time_end = "2017/6/"+str(day+1)+" 0:00"
                    else:
                        time_end = "2017/6/"+str(day)+" "+str(h)+":00:00"
                    sheet1.write(row_j,2,time_end,default_style)
                    cdn_down_traffic =  self.getRandom(1682)
                    sheet1.write(row_j,3,cdn_down_traffic,default_style)
                    box_up_traffic = self.getRandom(1869)
                    sheet1.write(row_j,4,box_up_traffic,default_style)
                    share_down_traffic= self.getRandom(15139)
                    sheet1.write(row_j,5,share_down_traffic,default_style)
                    row_j = row_j + 1
       ####生成7月份的数据
        for day in range(1,23):
            for h in range(1,25):
                for dev in range(0,1):   
                    sheet1.write(row_j,0,device[dev][0],default_style)
                    time_start = "2017/7/"+str(day)+" "+str(h-1)+":00:00"
                    sheet1.write(row_j,1,time_start,default_style)
                    time_end = ""
                    if h == 24:
                        if day == 30:
                            time_end = "2017/8/1"+" 0:00"
                        else:
                            time_end = "2017/7/"+str(day+1)+" 0:00"
                    else:
                        time_end = "2017/7/"+str(day)+" "+str(h)+":00:00"
                    sheet1.write(row_j,2,time_end,default_style)
                    cdn_down_traffic = self.getRandom(1682)
                    sheet1.write(row_j,3,cdn_down_traffic,default_style)
                    
                    box_up_traffic = self.getRandom(1869)
                    sheet1.write(row_j,4,box_up_traffic,default_style)
                    
                    share_down_traffic= self.getRandom(15139)
                    sheet1.write(row_j,5,share_down_traffic,default_style)
                    row_j = row_j + 1
        #for ii in res_all:
         #   sheet1.write(row_j,6,ii[6],self.set_style('Arial',220,False))
          #  row_j=row_j+1

        wbk.save('%s.xlsx' %sek)
        
    def getRandom(self,value):
        cent = random.randint(1,20)/100
        tmp = 0
        portion = random.randint(1,99)/100
        if random.randint(0,1) == 0:
            tmp = value*(1+cent)+portion
        else:
            tmp = value*(1-cent)+portion
        return tmp

    def __init__(self):
        print("hello world")
        self.export()
        

    def start(self, qid_export):
        
        #用这个来输出所有的excel
        for i in qid_export:
            self.export(i)

        self.cur.close()
        self.conn.close()

a = sqlToexcel();