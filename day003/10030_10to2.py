#!/usr/bin/env python
#-*-coding:utf-8-*-
a=input("请输入")
list=[]
while a>0:
    list.append(str(a%2))
    a/=2
while(len(list)):
    print list.pop(),