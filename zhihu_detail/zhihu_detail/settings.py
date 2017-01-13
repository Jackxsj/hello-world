# -*- coding: utf-8 -*-

# Scrapy settings for zhihu_detail project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'zhihu_detail'

SPIDER_MODULES = ['zhihu_detail.spiders']
NEWSPIDER_MODULE = 'zhihu_detail.spiders'

ITEM_PIPELINES = {  
    'zhihu_detail.pipelines.ZhihuDetailPipeline': 800, 
}


DOWNLOADER_MIDDLEWARES = {  
        'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware' : None,
        'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
        'zhihu_detail.spiders.rotate_useragent.RotateUserAgentMiddleware' :400  
}