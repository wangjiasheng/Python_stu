#!/usr/bin/env python
# coding:utf-8
try:
    fs=open("d:/1.txt","r+") #文件不存在
    print fs.readline()
except IOError:
    print "IOError"
else:
    fs.close()
