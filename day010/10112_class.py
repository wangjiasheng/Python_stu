#!/usr/bin/env python
# coding:utf-8
class User(object):
    '卧槽'
    x=100;
    @property
    def getUsername(self):
        return self.x;
    @getUsername.setter
    def setUsername(self,username):
        self.x=username
    @getUsername.deleter
    def deleteUsername(self):
        del self.x

print User.__dict__
print User.__doc__
print User.__name__
print User.__module__
print User.__bases__
