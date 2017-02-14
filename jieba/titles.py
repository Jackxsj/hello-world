# -*- coding: utf-8 -*-
import xlwt
import xlrd
import MySQLdb
import os


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
    print L

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
    print sum

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

if __name__ == "__main__":
    conn = MySQLdb.connect(
            host='localhost',
            user = 'root',
            passwd = 'root',
            port = 3306,
            charset='utf8')
    cur = conn.cursor()
    conn.select_db('zhihu')
    sek = 'table19551271'
    cur.execute('select * from %s' %sek);
    num_fields = len(cur.description)
    field_names = [i[0] for i in cur.description]
    
    #设置这个工作薄
    wbk = xlwt.Workbook()
    #设置这个sheet,所有的操作，都是在sheet上进行的
    sheet1 = wbk.add_sheet('test1',cell_overwrite_ok=True)
    for i in range(0,len(field_names)): 
        sheet1.write(0,i,field_names[i],set_style('Times New Roman',220,True))

    res_all = cur.fetchall()
    row_j=1
    for ii in res_all:
        sheet1.write(row_j,0,ii[0],set_style('Arial',220,False))
        sheet1.write(row_j,3,(ii[3]).strip('\n'),set_style('Arial',220,False))
        sheet1.write(row_j,4,ii[4],set_style('Arial',220,False))
        row_j=row_j+1

    wbk.save('%s.xlsx' %sek)

    cur.close()
    conn.close()

#快速获取这个column name
#import MySQLdb;
# conn = MySQLdb.connect(host='localhost',user = 'root',passwd = 'root',port = 3306,charset='utf8');
# cur = conn.cursor();
# conn.select_db('zhihu')
# num_fields = len(cur.description)
# field_names = [i[0] for i in cur.description]
# 
