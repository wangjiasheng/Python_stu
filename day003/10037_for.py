#!/usr/bin/env python
#-*-coding:utf-8
list=[8,3,7,1,9,3,8,1,5,2,6,87,3,6,7,3,6,8,5,3,6,9,2,3,5,1,6,7,9,3,5,9,6,3,6,8]
for i in range(len(list)):
    for j in range(i+1):
        if(list[i]<list[j]):
            list[j],list[i]=list[i],list[j]
    print list