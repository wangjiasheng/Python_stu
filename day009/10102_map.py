#!/usr/bin/env python
# coding:utf-8
def fun(value):
    return value*2
def fun1(value1,value2):
    return value1+value2
print map(fun,[1,2,3,4,5])
print map(fun1,[1,2,3],[1,2,3])
print map(lambda x,y:x+y,[1,2,4],[1,3,6])