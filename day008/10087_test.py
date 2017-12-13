#!/usr/bin/env python
# coding:utf-8
try:
    fs=open("c:/1.txt","w")
except IOError:
    fs.close()
    print "发生了异常"
finally:
    pass