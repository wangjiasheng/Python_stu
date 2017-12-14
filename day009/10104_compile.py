#!/usr/bin/python
# coding:utf-8
str="for i in range(0,20):print i"
c= compile(str,'',"exec")
print c,type(c)
eval(c)
exec(c)