#!/usr/bin/env python
# coding:utf-8
try:
    s=1/0;
except (IOError,ZeroDivisionError):
    print "异常"
else:
    print "没有发生异常"