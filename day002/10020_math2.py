#!/usr/bin/env python
#-*-coding:utf-8-*-
a = 0b001;
b = 0b101;
x =20;
y=20;
print "位运算符"
print a&b
print a|b
print a^b
print a,~a
print b,~b
print a,a << 1,a<<2
print b,b>>1,b>>2
print "逻辑运算符"
print True and True
print True or False
print not False
print "成员运算符"
list=[1,3,4,5,7,7,6,5,3,2,1];
print(2 in list)
print 4 not in list
print "身份验证符"
print x is y
print x is not y