# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 10:25:52 2018

@author: Administrator
"""

from threading import Thread
import time
def sayhi(name):
    time.sleep(2)
    print('%s say hello' %name)


class Sayhi(Thread):
    def __init__(self,name):
        super().__init__()
        self.name=name
    def run(self):
        time.sleep(2)
        print('%s say hello' % self.name)


if __name__ == '__main__':
    t = Sayhi('aaa')
    t.start()
    print('主线程')