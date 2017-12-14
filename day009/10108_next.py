#!/usr/bin/env python
# coding:utf-8
list1=iter([1,2,3,6,3,2,5,7,3,2,4,7,4,2,5,7,4,4,6,3,2,2,4,4,5,565,6,6])
while True:
    try:
        x=next(list1)
        print x;
    except StopIteration:
        print "Error"
        break