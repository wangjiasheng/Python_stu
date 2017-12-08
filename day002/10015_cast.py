#!/usr/bin/env python
#-*-coding:utf-8-*-

#int
x="100" #int(x) 将x转换成为一个整数
y=1
print x,type(int(x))   #将字符串转换成整形
print x,type(float(x)) #将字符串转换成flaot
print x,type(long(x))  #将字符串转换成long
print complex('1+2j') #将字符串转换成复数
print  y,type(str(y))  #数字转化成字符串
print type(repr([1,5,6,7,3])) #将对象转换成字符串
print type(eval("[1,4,6,3,6,9,2,5,4,3]"))#将字符串转换成对象
print type(tuple([2,3,4,5,6,7]))             #将数组转换成元组
print type(list((1,2,3,4,5,6)))              #将元组转换成数组
print type(set((2,3,4,5,6,7,8,3)))           #将list转换成集合
print type(dict(eval("{'2':'4'}")))        #将字典转换成字典
print type(frozenset((2,3,4,5,6,3)))         #将元组转换成不可变数组
print chr(97),chr(122)                       #将数字转换成ASCII
print chr(65),chr(90)                        #将数字转换成ASCII
print unichr(97)                             #将数字转化成Unicode
print ord('a')                               #将ASCII转换成数字
print hex(97)                                #将数字转换成16进制
print oct(97)                                #将数字转换成8进制