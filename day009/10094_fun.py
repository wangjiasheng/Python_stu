#!/usr/bin/env python
#coding:utf-8
class C(object):
    def __init__(self):
        self._x=None
        print self
    def getx(self):
        print "getX"
        return self._x
    def setx(self,value):
        print "setX"
        self._x=value
    def delx(self):
        print "delValue"
        del self._x
    def doc(self,value):
        self.doc=value
    x=property(getx,setx,delx,"卧槽")
#测试
s=C();
s.x=10;
print s.x
del s.x
print s.__doc__


