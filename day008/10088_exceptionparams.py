#!/usr/bin/env python
# coding:utf-8
try:
    fs=open("c:/1.txt","w+")
except IOError,params:
    print params
finally:
    print "执行结束"