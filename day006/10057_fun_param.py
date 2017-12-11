#!/usr/bin/env python
#coding:utf-8
#必备参数，调用时没有参数报错
def println(params):
    print params
    return
println("卧槽")
#关键字参数可以不按顺序出牌
def println(username,age):
    print username,age
    return
println(age=20,username="wjs")
#缺省参数
def println(username="wjs",age=20,sex="男"):
    print username,age,sex
    return;
println()