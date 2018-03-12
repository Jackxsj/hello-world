# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 13:40:13 2017

@author: Administrator
"""

import redis
 r = redis.Redis(host='30.254.180.182', port=6379, db=4) 
 r.memget('18180413624')
 print(r)