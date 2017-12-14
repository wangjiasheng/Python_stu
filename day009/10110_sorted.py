#!/usr/bin/env python
# coding:utf-8
def so(param1,param2):
    s=cmp(param1,param2)
    return param1-param2;
list2=[2,3,4,6,8,9,9,0,4,3,65,3,4,74]
print sorted(list2,so)

list2=[('b',2),('a',1),('c',3),('d',4)]
print sorted(list2, cmp=lambda x,y:cmp(x[1],y[1]))
print sorted(list2,cmp=lambda x,y:x[1]-y[1])
print sorted(list2,key=lambda s:s[1]) #如果不标明默认以cmp如果表面默认以标明值


