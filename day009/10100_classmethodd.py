#!/usr/bin/env python
# coding:utf-8
class A(object):
    z=1;
    def println(woao):
        print "method"
    @classmethod
    def printyy(cls):
        print cls.z
        print cls().println()
A.printyy()
print A.z
print"----------------"
class User:
    def __init__(self,value):
        self.a=value
    @property
    def x(self):
        return self.a
    @x.setter
    def x(self,value):
        self.a=value
    @x.deleter
    def x(self):
        del self.a
user1=User(3)
user2=User(3)
user1.a=10;
user2.a=20;
print user1.a,user2.a