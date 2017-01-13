# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs
import re

import MySQLdb

from zhihu.spiders.zhihu_spider import *
from zhihu.getInteresting import *


class ZhihuPipeline(object):
    def __init__(self):
        # self.write_file = codecs.open('out.json', 'wb', 'utf-8')
        
        self.conn = MySQLdb.connect(
                host = 'localhost',
                user='root',
                passwd='root',
                port=3306)
        self.cur = self.conn.cursor()
        try:
            self.cur.execute('create database if not exists zhihu')
        except MySQLdb.Error, e:
            print 'Mysql error %d: %s' % (e.args[0], e.args[1])
        self.conn.select_db('zhihu')
        try:
            print 'create table here'
            self.cur.execute('create table %s(aid int, zan int,  publish_time int, title varchar(512), content varchar(5120), PRIMARY KEY (aid))' % ZhihuSpider.my_parse.table) # 主键
        except MySQLdb.Error, e:
            print 'Mysql error %d: %s' % (e.args[0], e.args[1])
    def process_item(self,item,spider):
        res_dict = dict(item)
        value = []
        print 'res_dict is:'
        print res_dict
        for it in res_dict:
            print 'processing defined by Jack'
            if cmp(it,'qid')==0:
                result = re.search("\d+",str(res_dict[it]))
                #print 'result is'
                #print result.group(0)
                value.append(result.group(0))
                value.append(0)
                value.append(0)
            elif cmp(it, 'url_link') == 0 or cmp(it, 'title') == 0:
                reslut = re.findall("'(.*?)'", repr(res_dict[it]),re.S)
                res_str = ''
                for i in reslut:
                    res_str = '%s%s' % (res_str, i)
                
                # 打印出问题。
                #print 'res_str is as followed:'
                #print res_str.decode('utf-8')
                value.append(res_str)
        value[3],value[4] = value[4],value[3]
        value.append(0)
        print value
        insert_command = 'insert into %s values' % ZhihuSpider.my_parse.table
        try:
            print 'begin to insert'
            self.cur.execute(insert_command + '(%s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE zan=%s', value)
        except MySQLdb.Error, e:
            print 'Mysql error %d: %s' % (e.args[0], e.args[1])
        self.conn.commit()
        print 'after inserted'
        return item
        
    def process_item_1111(self, item, spider):
        #line = json.dumps(dict(item)) + "\n"
        #uni_info = line.decode('unicode_escape')
        #pattern = re.compile(' +|\t+')
        #out = pattern.sub(' ', uni_info)
        #self.write_file.write(out)
        res_dict = dict(item)
        value = []
        for it in res_dict:
            print 'process_item dealing here.........'
            print it
            if cmp(it, 'content') == 0 or cmp(it, 'title') == 0:
                reslut = re.findall("'(.*?)'", repr(res_dict[it]).decode('unicode_escape').encode('utf-8'), re.S)
                res_str = ''
                for i in reslut:
                    res_str = '%s%s' % (res_str, i)
                    
                # 打印出问题。
                if cmp(it, 'title') == 0:
                    print res_str
                    
                value.append(res_str)
            elif cmp(it, 'zan') == 0 or cmp(it, 'publish_time') == 0 or cmp(it, 'aid') == 0:
                reslut = re.search("'(\d+)'", str(res_dict[it]))
                value.append(reslut.group(1))
        print '*' * 10
        # 交换 aid 和 content
        value[0], value[4] = value[4], value[0]
        
        #只更新赞同的人数
        value.append(value[1])
        # value = [self.table] + value
        insert_command = 'insert into %s values' % ZhihuSpider.my_parse.table
        self.cur.execute(insert_command + '(%s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE zan=%s', value)
        
        return item
        
    def close_spider(self, spider):
       # GetInteresting().start()
       print 'close'
    
