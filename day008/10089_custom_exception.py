#!/usr/bin/env python
# coding:utf-8
class NetworkError(RuntimeError):
    def __init__(self,value):
        print "类型:",type(value)
        self.args=value
    def __str__(self):
        return "".join(self.args) #将tuple转换成字符串
try:
    raise NetworkError("i am 去了个球")
except NetworkError,params:
    print params
finally:
    print "完毕"