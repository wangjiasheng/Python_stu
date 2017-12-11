#!/usr/bin/env python
# coding:utf-8
import time
print time.altzone
print time.asctime()
print time.ctime()
print time.clock()
print time.gmtime()  # 格林威治天文时间
print time.localtime()
print time.mktime(time.localtime(time.time()))
time.sleep(1)
print "暂停结束"
print time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
print time.strptime("2015-10-12 3:45:33","%Y-%m-%d %H:%M:%S")
print time.time()
