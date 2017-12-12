#!/usr/bin/env python
#coding:utf-8
fo = open("d:/1.txt","wb")
print "文件名:",fo.name
print fo.closed
print fo.mode
print fo.softspace
fo.close();
print fo.closed