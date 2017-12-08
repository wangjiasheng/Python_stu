#!/usr/bin/env python
#-*-coding:utf-8-*-
print "is 和 ==区别"
a=[1,2,3]
b=a;
c=a[:] #list对象拷贝
print a is b ,a == b
print a is c ,a == c
print "特殊示例交互模式"
m=10;n=10;
x=10;
print m is n,m is x   #交互模式为false
print m==n,m==x        #任何模式都是true