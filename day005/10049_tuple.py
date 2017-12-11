#!/usr/bin/env python
#-*-coding:utf-8-*-
tuple1=(1)
print type(tuple1)
tuple1=(1,)
print type(tuple1) #区别蛮大的
#元组的运算符
tuple1=(1,2,3,4,5)
tuple2=(6,7,8,9,10)
print len(tuple1)
print tuple1+tuple2 #元组不能修改但是能合并生成新的元组
print tuple1*2
print 1 in tuple1 ,1 in tuple2
for x in tuple1:
    print x
#元组的截取
print tuple1[2:]
print tuple1[-1]
print tuple1[:2]
print tuple1[-3:-1]
#任意无符号的对象，以逗号隔开，默认为元组
s= 'abc', -4.24e93, 18+6.6j, 'xyz'
print type(s);
#tuple内置函数
print cmp(tuple1,tuple2)
print len(tuple1)
print max(tuple1)
print min(tuple1)
print tuple(tuple1)