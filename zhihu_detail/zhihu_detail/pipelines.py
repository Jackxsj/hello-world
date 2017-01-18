# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs
import re

import MySQLdb
from zhihu_detail.spiders.zhihu_detail_spider import *

class ZhihuDetailPipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect(
                host = 'localhost',
                user='root',
                passwd='root',
                port=3306,
                charset='utf8')
        self.cur = self.conn.cursor()
        try:
            self.conn.select_db('zhihu')
        except MySQLdb.Error, e:
            print 'Mysql error %d: %s' % (e.args[0], e.args[1])
    
    def process_item(self,item,spider):
        res_dict = dict(item)
        value = []
        key_map=['qid','aid','zan_num','people','people_url','content','img_link','pb1','pb2']
        for it in key_map:
            
            if cmp(it,'qid')==0:
                print it
                value.append(res_dict[it])
            elif cmp(it,'aid')==0:
                print it
                value.append(res_dict[it])
            elif cmp(it,'zan_num')==0:
                print it
                value.append(res_dict[it])
            elif cmp(it,'people')==0:
                print it
                value.append((res_dict[it]).encode('utf-8'))
            elif cmp(it,'people_url')==0:
                print it
                value.append('') #url need js feature to get, not implement yet
            elif cmp(it,'content')==0:
                print it
                value.append((res_dict[it]).encode('utf-8'))
            elif cmp(it,'img_link')==0:
                print it
                value.append(res_dict[it]) #img_link is string here
            elif cmp(it,'pb1')==0:
                print it
                value.append(0) #backup
            elif cmp(it,'pb2')==0:
                print it
                value.append((''))#backup
        value.append(res_dict['zan_num'])
        #TODO: checking failed to write to sql
        table_name = 'q'+res_dict['qid']
        insert_command = 'insert into %s values' %table_name
        print insert_command
        try:
            print 'begin to insert'
            #self.cur.execute(insert_command + '(%s,%s,%s,%s,NULL,NULL,NULL,NULL,NULL) ON DUPLICATE KEY UPDATE zan_num=%s ', value)
            self.cur.execute(insert_command + '(%s,%s,%s,%s,%s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE zan_num=%s', value)
        except MySQLdb.Error, e:
            print 'Mysql error %d: %s' % (e.args[0], e.args[1])
        self.conn.commit()
        print 'after inserted'
        return item
