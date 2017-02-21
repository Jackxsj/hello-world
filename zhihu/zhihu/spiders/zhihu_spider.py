# -*- coding:utf-8 -*-
import re

from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor as sle

from zhihu.items import *
from zhihu.util import *
#引入request的选项方便修改http请求
from scrapy.http import Request

class ZhihuSpider(CrawlSpider):
    my_parse = MyParse()
    download_delay = 1.2
    name = 'zhihu'
    start_urls = [ my_parse.topic_url ]
    allowed_domains = ['zhihu.com']
    print my_parse.pages
    rules = [
        #测试!!!，把下面的这个Rule注释掉，并设置follow=true，在新的链接里parse
        #Rule(sle(allow = ('/question/\d+$', )), callback = 'prase_info', follow = False),
        #Rule(sle(allow = ('/%s/questions/$' % my_parse.link_id, )), follow = True),
        #测试结束
        
        #这个是给那个链接加上？sort=created, 这里有两个调用方法，这里用来终结，不再继续爬取，所以这里的rules控制了爬取过程
        Rule(sle(allow = ('/question/\d+$', )), callback= 'prase_test',process_request='parse_feature',follow = False),
        #从1-2页，这里利用了scrapy自己的特性即爬取每一页上面的链接，这里用来控制一共有几页，上面的那个callback和process_request是终结，不再继续爬取
        Rule(sle(allow = ('\?page=([1-2])$', )), follow = True),
        #从1-50页
        #Rule(sle(allow = ('\?page=([1-4]?\d|50)$', )), follow = True),
    ]
    #/question/\d+\?sort=created&page=\d+$
    
    #def parse(self, response): 
    #    print response.body
       
    #http://blog.csdn.net/dawnranger/article/details/50037703
    #这个selector需要判断是如何使用的
    #这个是回来匹配上的就会去收集
    def prase_info(self, response):
        """解析回答信息"""
        print 'matched and called parse_info here'
        sel = Selector(response)
        tmp_title = sel.xpath('//title/text()').extract()
        print 'begin to check the title info here'
        print tmp_title[0]
        for sel in response.xpath('//div[@class="zm-item-answer  zm-item-expanded"]'):
            item = ZhihuItem()
            item['title'] = tmp_title[0].encode('utf-8')
            item['content'] = sel.xpath('div[@data-action]/div/text()').extract()
            print 'check the content fetched or not'
            item['zan'] = sel.xpath('div/button/span[@class="count"]/text()').extract()
            item['publish_time'] = sel.xpath('@data-created').extract()
            item['aid'] = sel.xpath('@data-aid').extract()
            
            zan_str = re.search("'(.*?)'", unicode(item['zan']))
            print '-' * 15
            print zan_str.group(1)
            print '-' * 15

            # 赞大于zan_th的回答才是需要的
            if int(zan_str.group(1)) >= ZhihuSpider.my_parse.zan_th:
                yield item
                
    def prase_test2(self,response):
        print 'get response here2'
        print 'request url is'
        sel = Selector(response)
        temp_title = sel.xpath('//title/text()').extract()
        for sel in response.xpath('//div[@class="zg-wrap zu-main clearfix with-indention-votebar"]'):
            print 'matched in sel...'
            item = detailQuestionItem()
            item['title'] = temp_title
            item['qid'] = sel.xpath('//@data-urltoken').extract()        
            item['url_link'] = response.url
            print item['title']
            print item['url_link']
            print item['qid']
        
    def prase_test(self,response):
        print 'get response here1'
        print 'request url is'
        sel = Selector(response)
        item = detailQuestionItem()
        item['title'] = ((sel.xpath('//title/text()').extract())[0])
        item['qid'] = (sel.xpath('//div[@class="zg-wrap zu-main clearfix with-indention-votebar"]/@data-urltoken').extract())[0]
        item['url_link'] = response.url
        print item['title']
        print item['url_link']
        print item['qid']
        return item
        
        
        
    def parse_feature(self,request):
        print 'test add_feature here...........'
        original_url = request.url
        new_url= original_url + "?sort=created"
        request=request.replace(url=new_url)
        print request.url
        return request