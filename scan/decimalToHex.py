# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 10:59:15 2018

@author: Administrator
"""

s = "29.48.88.128"
def decToHex(num):
    if num <10:
        return str(num)
    s = {
            10:'a',
            11:'b',
            12:'c',
            13:'d',
            14:'e',
            15:'f'            
        }
    return s.get(num)

s_sp = s.split('.')
print(s_sp)
hex_s = ""
for i in s_sp:
    j=int(int(i)/16)
    k=int(i)%16    
    hex_s = hex_s+decToHex(j)+decToHex(k)+":"
s_convert = hex_s.strip(':')
print(s_convert)