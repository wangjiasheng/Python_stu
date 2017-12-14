#!/usr/bin/env python
# coding:utf-8
class Vct:
    def __init__(self,x,y):
        self.x=x;
        self.y=y;
    def add(self,other):
        return Vct(self.x+other.x,self.y+other.y)
    def __str__(self):
        return "Vct(%d,%d)" % (self.x,self.y)

v=Vct(1,5)
s=Vct(3,2)
print v.add(s)