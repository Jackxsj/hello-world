# -*- coding:utf-8 -*-
import re

from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor as sle

#保证引用正确，否则会出现找不到spider的情况
from zhihu_detail.items import *
from zhihu_detail.util import *
#引入request的选项方便修改http请求
from scrapy.http import Request

class ZhihuDetailSpider(CrawlSpider):
    my_parse = MyParse()
    download_delay = 0.8
    name = 'zhihu_detail'
#    start_urls = my_parse.url_link
    start_urls = ['https://www.zhihu.com/question/23427617?sort=created']
    allowed_domains = ['zhihu.com']
    
    rules = [
        #针对sort=created的页面只用根据page来parse信息
        Rule(sle(allow = ('\&page=[1-2]$', )), callback= 'prase_info',follow =False),
    ]
    def prase_info(self, response):
        """解析回答信息"""
        print 'matched and called parse_info here'
        sel = Selector(response)
        tmp_qid = (sel.xpath('//div[@class="zg-wrap zu-main clearfix with-indention-votebar"]/@data-urltoken').extract())[0]
        print tmp_qid
        #使用//注意是从根节点开始定义，这里已经用sel过滤一次后，内循环不需要/
        for sel in response.xpath('//div[@class="zm-item-answer  zm-item-expanded"]'):
            item = ZhihuDetailItem()


             #匿名用户处理
            tmp_p = ''
            tmp_p2 = ''
            
            if sel.xpath('div/div/span[@class="name"]'):
                tmp_p = sel.xpath('div/div[@class="zm-item-answer-author-info"]/span[@class="name"]/text()').extract()
                #tmp_p = sel_tmp.xpath('span[@class="name"]/text()').extract()
                print tmp_p

            if sel.xpath('div[@class="answer-head"]/div[@class="zm-item-answer-author-info"]/a[@class="zm-item-link-avatar avatar-link"]'):
                print 'checking tmp_p2'
                tmp_p2 = sel.xpath('div/div/a[@class="zm-item-link-avatar avatar-link"]/@href').extract()
                #tmp_p2 = sel.xpath('div/div/span[@class="summary-wrapper"]/span/a[@class="author-link"]/@href').extract()
                print tmp_p2
                
            item['qid'] = tmp_qid
            print item['qid']
            item['aid'] = (sel.xpath('@data-atoken').extract())[0]
            print item['aid']
            item['zan'] = (sel.xpath('div/button/span[@class="count"]/text()').extract())[0]
            print item['zan']
           

                    
            if tmp_p :
                item['people'] = tmp_p[0]
            elif tmp_p2:
                item['people'] = tmp_p2[0]
            else:
                item['people'] = '匿名用户'
            print item['people']

            tmp_content=''.join(sel.xpath('div/div[@class="zm-editable-content clearfix"]/node()').extract())
            item['content'],num = re.subn('<br>','\\n',tmp_content)
            print item['content']
            #TODO: 看下为什么不能打出下面的img链接
            #TODO2: 返回item
            #TODO3: myParse 创建表
            #TODO4: itemPipline写入
            #TODO5: 测试
            tmp_img_link = ''
            for sel_img in sel.xpath('div/div[@class="zm-editable-content clearfix"]/img'):
                print 'check img'
                if sel_img.xpath('@data-original'):
                    tmp_img_link = tmp_img_link +';;'+(sel_img.xpath('@data-original').extract())[0]
            for sel_img in sel.xpath('div/div[@class="zm-editable-content clearfix"]/b/img'):
                print 'check img in block'
                if sel_img.xpath('@data-original'):
                    tmp_img_link = tmp_img_link +';;'+(sel_img.xpath('@data-original').extract())[0]
        
            item['imglink']=tmp_img_link
            print item['imglink']
            print '-' * 60

            # 赞大于zan_th的回答才是需要的
         #   if int(item['zan']) >= ZhihuDetailSpider.my_parse.zan_th:
        #        yield item
                