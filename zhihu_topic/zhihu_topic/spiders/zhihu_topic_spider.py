# coding:utf-8
import re

from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor as sle

from zhihu_topic.items import *

class TopicSpider(CrawlSpider):
    download_delay = 0.8
    #这个名字是scrapy crawl的运行时需要提供的
    name = 'topic'
    #start_urls = ['http://www.zhihu.com/topic/19776749']
    #使用下面的知识管理作为首先测试的环节，这个其实只是设置目录
    start_urls = ['https://www.zhihu.com/topic/19556758']
    allowed_domains = ['zhihu.com']
    #先注释下面的parse全部，只parse这个topic下的；另外注意callback后面的方法名不能使用parse，需要用具体的名字
    #http://www.jianshu.com/p/83c73071d3cb
    #rules = [Rule(sle(allow = ('/topic/\d+$', )), callback = 'parse_topic', follow = True),]
    rules = [Rule(sle(allow = ('/topic/19556758$', )), callback = 'parse_topic', follow = True),]
    
    def parse_topic(self, response):
        sel = Selector(response)
        item = ZhihuTopicItem()
        item['topic'] = sel.xpath('//h1[@class="zm-editable-content"]/text()').extract()
        #rfind找到最后一次出现的位置
        #收集的时候的那个网址是https://www.zhihu.com/topic/19556758/hot 即index-1
        index1 = response.url.rfind('/')
        index2 = response.url.rfind('/',0,index1)
        item['link_id'] = response.url[index2+1:index1]
        item['followers'] = sel.xpath('//div[@class="zm-topic-side-followers-info"]/strong/text()').extract()
        item['paren_topic'] = sel.xpath('//div[@id="zh-topic-side-parents-list"]/div/div/a/text()').extract()
        item['child_topic'] = sel.xpath('//div[@id="zh-topic-side-children-list"]/div/div/a/text()').extract()
        print repr(item).decode('unicode-escape')
        print '*' * 20
        return item
        
    
    
    
    
    