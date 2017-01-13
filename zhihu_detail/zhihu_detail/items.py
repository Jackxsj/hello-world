# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhihuDetailItem(scrapy.Item):
    # define the fields for your item here like:
    qid = scrapy.Field()
    aid = scrapy.Field()
    zan = scrapy.Field()
    people = scrapy.Field()
    content = scrapy.Field()
    imglink = scrapy.Field()
    bkp1 = scrapy.Field()
    bkp2 = scrapy.Field()
    pass
