#!/usr/bin/env python
# coding:utf-8
def multi(x,y):
    return x*y
def add(x,y):
    return x+y
print reduce(add,[1,2,3,4,5])
print reduce(multi,[1,2,3,4,5])