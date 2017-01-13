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
    def process_item(self, item, spider):
        return item
