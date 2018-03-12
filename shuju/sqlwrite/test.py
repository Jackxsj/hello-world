# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 16:31:32 2017

@author: Administrator
"""

import MySQLdb
import os

class sqlToexcel:  
    def export(self,que_one):
        sek = que_one
        self.cur.execute('select * from %s' %sek);
        num_fields = len(self.cur.description)
        field_names = [i[0] for i in self.cur.description]
        
        #设置这个工作薄
        wbk = xlwt.Workbook()
        #设置这个sheet,所有的操作，都是在sheet上进行的
        sheet1 = wbk.add_sheet('test1',cell_overwrite_ok=True)
        for i in range(0,len(field_names)): 
            sheet1.write(0,i,field_names[i],self.set_style('Times New Roman',220,True))

        res_all = self.cur.fetchall()
        row_j=1
        for ii in res_all:
            sheet1.write(row_j,0,ii[0],self.set_style('Arial',220,False))
            sheet1.write(row_j,1,ii[1],self.set_style('Arial',220,False))
            sheet1.write(row_j,2,ii[2],self.set_style('Arial',220,False))
            sheet1.write(row_j,3,ii[3],self.set_style('Arial',220,False))
            sheet1.write(row_j,5,ii[5],self.set_style('Arial',220,False))
            sheet1.write(row_j,6,ii[6],self.set_style('Arial',220,False))
            row_j=row_j+1

        wbk.save('%s.xlsx' %sek)

    def __init__(self):
        self.conn = MySQLdb.connect(
                host='30.254.226.177',
                user = 'jfwx',
                passwd = 'root123',
                port = 3306,
                charset='utf8')
        self.cur = self.conn.cursor()
        self.conn.select_db('radius')

    def start(self, qid_export):
        
        #用这个来输出所有的excel
        for i in qid_export:
            print i
            self.export(i)

        self.cur.close()
        self.conn.close()