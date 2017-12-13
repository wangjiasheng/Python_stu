#!/usr/bin/env python
# coding:utf-8
try:
    fs=open("c:/1.txt","w+");#文件权限不存在
    fs.write("卧槽");
except IOError:
    print "权限不允许"
else:
    fs.close();