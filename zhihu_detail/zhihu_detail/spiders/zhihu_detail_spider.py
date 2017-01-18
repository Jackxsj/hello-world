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
#power shell 日志命令
#Start-Transcript -path d:\soft\python\powershelllog.txt -Force -Append –NoClobber
class ZhihuDetailSpider(CrawlSpider):
    my_parse = MyParse()
    #这个必须小写，能够控制每个request的抓取时间
    download_delay = 2 
    name = 'zhihu_detail'
#    start_urls = []
    start_urls = my_parse.url_link
    print my_parse.url_link
    
    allowed_domains = ['zhihu.com']
    
    #rules = [
        #针对sort=created的页面只用根据page来parse信息
        #follow=True后会生成page=1,2等页面 
        #Rule(sle(allow = ('\&page=[1-2]$', )), callback= 'prase_info',follow =True),
    #    Rule(sle(allow = ('\&page=([1-4]?\d|50)$', )), callback= 'prase_info',follow =True),
    #]
    def start_requests(self):
            for url in self.start_urls:
                print(url)
                for i in range(0,50):
                    tmp_url = url+'&page='+str(i)
                    yield Request(tmp_url, callback = self.prase_info)
                
    def prase_info(self, response):
        """解析回答信息"""
        print 'matched and called parse_info here'
        sel = Selector(response)
        tmp_qid = (sel.xpath('//div[@class="zg-wrap zu-main clearfix with-indention-votebar"]/@data-urltoken').extract())[0]
        print tmp_qid
        #使用//注意是从根节点开始定义，这里已经用sel过滤一次后，内循环不需要/
        for sel in response.xpath('//div[@class="zm-item-answer  zm-item-expanded"]'):
            item = ZhihuDetailItem()
            item['qid'] = tmp_qid
            print item['qid']
            item['aid'] = (sel.xpath('@data-atoken').extract())[0]
            print item['aid']
            tmp_zan = (sel.xpath('div/button/span[@class="count"]/text()').extract())[0]
            #当过万赞后需要把这个12K取代掉
            zan_str,tmp_num = re.subn('K','000',tmp_zan)
            item['zan_num']=zan_str
            print item['zan_num']
           

             #匿名用户处理，这里一些用户的href_link是在那个js里面，后面需要单独处理
            #TODO: 后面把用户的link单独处理
            tmp_p = ''
            if sel.xpath('div[@class="zm-item-rich-text expandable js-collapse-body"]/@data-author-name'):
                tmp_p = sel.xpath('div[@class="zm-item-rich-text expandable js-collapse-body"]/@data-author-name').extract()
            if tmp_p :
                print tmp_p[0].__class__
                item['people'] = tmp_p[0]
            print item['people']

            tmp_content=''.join(sel.xpath('div/div[@class="zm-editable-content clearfix"]/node()').extract())
            item['content'],num = re.subn('<br>','\\n',tmp_content)
            print item['content'].__class__
            #TODO: 看下为什么不能打出下面的img链接---完成：有些位于block里面
            #TODO2: 返回item-------完成：使用yield item
            #TODO3: myParse 创建表
            #TODO4: itemPipline写入
            #TODO5: 测试
            tmp_img_link = ''
            for sel_img in sel.xpath('div/div[@class="zm-editable-content clearfix"]/img'):
                if sel_img.xpath('@data-original'):
                    tmp_img_link = tmp_img_link +';;'+(sel_img.xpath('@data-original').extract())[0]
            for sel_img in sel.xpath('div/div[@class="zm-editable-content clearfix"]/b/img'):
                if sel_img.xpath('@data-original'):
                    tmp_img_link = tmp_img_link +';;'+(sel_img.xpath('@data-original').extract())[0]
            if isinstance(tmp_img_link, unicode):
                item['img_link']=tmp_img_link.encode('utf-8')
            else:
                item['img_link']=tmp_img_link
            #这个是str 类型，即本来就是utf-8的类型
            print item['img_link'].__class__
            

            # 赞大于zan_th的回答才是需要的
            if int(item['zan_num']) >= 0:
                print 'yield item here'
                yield item
            print '-' * 60    