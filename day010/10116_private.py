#!/usr/bin/env python
# coding:utf-8
class JustCounter:
    __secretCount=0;
    pricount=0;
    def count(self):
        self.__secretCount+=1;
        self.pricount+=1
        print self.__secretCount
counter=JustCounter()
counter.count()
counter.count()
print counter.pricount
print counter._JustCounter__secretCount #一个横岗开头