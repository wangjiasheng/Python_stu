#!/usr/bin/env python
# coding:utf-8
s= frozenset([1,2,3,4,5,6,7])

class A(object):
    bar=1;
    def __init__(self):
        pass
    @property
    def x(self):
        return self.username
    @x.setter
    def x(self,value):
        self.username=value
    @x.deleter
    def x(self):
        del self.username
a = A()
a.username="卧槽"
print getattr(a,"bar")
print getattr(a,"username")