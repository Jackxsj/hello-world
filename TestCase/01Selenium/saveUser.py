# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 16:22:34 2018

@author: Administrator
"""

# -*- coding: utf-8 -*-
from selenium import webdriver
import time
import os


for n in range(3,4):
    dr = webdriver.Firefox()
    var_mobile = '18888880000'+str(n)
    var_name = '%E6%B5%8B%E8%AF%95'+str(n)
    print(var_mobile)
    print(var_name)
    file_path =  'http://192.168.1.91:12346/management/advertiser/save?username={mobile}&nickname={name}&type=1&password=x111111'\
        .format(mobile=var_mobile,name=var_name)
    
    
    response = dr.request('POST', file_path)
    print(response)
    


    time.sleep(1)
    dr.close(file_path)

    dr.quit()