# -*- coding: utf-8 -*-
import scrapy


class Py3zhihuSpider(scrapy.Spider):
    name = 'py3zhihu'
    allowed_domains = ['zhihu.com']
    start_urls = ['http://zhihu.com/']

    def parse(self, response):
        pass
