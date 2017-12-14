#!/usr/bin/env python
# coding:utf-8
s=repr([2,4,3,1,7,3,9,3,7])
print s,type(s),eval(s),type(eval(s))
print range(0,2)
print xrange(3,6),list(xrange(3,6))
print cmp(23,1)
print globals()
print max([1,2,3,4,5,6,7,8,45,3])
print list(reversed([1,2,4,2,4,2,4,6,4,2,5]))


list1=[1,2,3,4]
list2=[2,3,4,5,6]
com=zip(list1,list2);
print com
print zip(*com)

