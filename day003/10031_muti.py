#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 九九乘法表

i=1
while i:
    j = 1
    while j:
        print str(i)+"*"+str(j)+"="+str(i*j),
        if(i==j):
            break;
        j=j+1;
    print
    i+=1
    if(i>9):
        break