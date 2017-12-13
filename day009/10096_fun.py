#!/usr/bin/env python
#coding:utf-8
print tuple("fldlfld")
print bool(1),bool(2),bool(0)
print issubclass(bool,int)

def is_1(params):
    if(params==1):
        return True
    return False
listv=[1,2,3,3,1,2,4,6,1,3,1,4,1]
print filter(is_1,listv)

print len("ddddddddd")
print range(0,10)
print range(10)
print range(0,10,2)
print range(0,-10,-2)

print bytearray([1,3,4,5,6])

print callable(is_1)

class A:
    def hh(self):
        print "wocao"
        pass
A.hh()
