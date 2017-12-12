#!/usr/bin/env python
#coding:utf-8
age=10
def multi(age):
    age=20;
    print "局部变量",age;
multi(20)
print "全局变量",age;