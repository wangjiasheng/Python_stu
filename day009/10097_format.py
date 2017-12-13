#!/usr/bin/env python
# coding:utf-8
#method1
print "{}__{}".format("卧槽","高手")
#method2
print "{0},{1}".format("哈哈","兄啊")
#method3
print "{1},{0},{1}".format("yes","no")
#method4
print "{username},{passwrod}".format(username="卧槽",passwrod="哈哈")
#method5
dict1={"username":"wjs","password":"812330500"}
print "姓名:{username},密码:{password}".format(**dict1)
#method6
my_list=["wjs","812330500"]
print "姓名:{0[0]},密码:{0[1]}".format(my_list)
#method7
class AssignValue(object):
    def __init__(self,value):
        self.result=value
value=AssignValue(6);
print "value is {0.result}".format(value)
print value.result