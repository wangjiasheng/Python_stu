#!/usr/bin/env python
# coding:utf-8
class D(object):
    def __init__(self):
        self._x=None
    @property
    def x(self):
        print "get"
        return self._x
    @x.setter
    def x(self,value):
        print "set"
        self._x=value
    @x.deleter
    def x(self):
        print "del"
        del self._x
s=D()
s.x=100;
print s.x
del s.x