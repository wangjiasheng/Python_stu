#!/usr/bin/env python
#coding:utf-8
def funx(x):
    def funy(y):
        return x * y;
    return funy
print type(funx(7)(8)),funx(7)(8)