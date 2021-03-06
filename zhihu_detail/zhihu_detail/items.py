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
    zan_num = scrapy.Field()
    people = scrapy.Field()
    people_url = scrapy.Field()
    content = scrapy.Field()
    img_link = scrapy.Field()
    bkp1 = scrapy.Field()
    bkp2 = scrapy.Field()
    pass
