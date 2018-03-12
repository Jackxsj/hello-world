# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 15:45:42 2018

@author: Administrator
"""

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

dr = webdriver.Chrome()
print('maximize browser')
dr.maximize_window()

url = 'http://192.168.1.5:2080/index.html#system/serviceMgt/serviceMgt.html'

dr.get(url)

print( dr.get_cookies())
dr.delete_all_cookies()
dr.add_cookie({'name': 'JSESSIONID', 'value': '1B5B2355EC595B3F2C99BD322490FD91'})
dr.add_cookie({'name': 'SESSION', 'value': 'b3aa9cc5-6a13-498e-a735-2ff723857b65'})

dr.get(url)

#睡眠2S,避免页面还没加载出来
time.sleep(2)
dr.find_element_by_id('add').click()


