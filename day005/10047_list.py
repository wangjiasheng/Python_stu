#!/usr/bin/env python
#-*-coding:utf-8-*-
list1=[1, 2, 3, 4, 5, 6, 7, 8]
tuple=(1,2,3,4,5,6,7,8)
print list1
list1[1]=28;
print list1
del list1[1]
print list1
#python脚本操作符
print list1 * 2     #重复
print list1 + list1  #组合
print len(list1)
print list1, "wjs" in list1
print "-----------------------"
for x in [1,2,3]:
    print x
print "-----------------------"
#python截取
print "list[-1]",list1[-1]
print "list[1:]", list1[1:]
print "list[:4]", list1[:4]
print "-----------------------"
#python函数
print cmp(list1, tuple)
print len(list1)
print max(list1)
print min(list1)
print tuple,list(tuple)
#python方法
print list1,list1.append(100),list1
print list1.count(1)
print list1.extend([34,65,34,23]),list1
print list1,list1.index(5)
print list1.insert(2,200),list1
print "-----------------------POP-------------------------"
print list1
list1.pop()
print list1
list1.pop(2)#删除的是下标对应的值
print "-----------------------Remove----------------------"
print list1
list1.remove(1) #删除的是值
print list1
print "---------------------Reverse-----------------------"
print list1
list1.reverse()
print list1
print "------------------------Sort------------------------"
print list1
list1.sort()
print list1