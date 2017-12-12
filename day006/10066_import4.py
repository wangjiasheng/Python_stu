#!/usr/bin/env python
# coding:utf-8
import math
import addutils.modeltest
show=dir(math)
print show
print dir(addutils.modeltest)
print "------------------------------------------------------------------"
print globals() #返回的是所有在该函数里能访问的全局名字
print locals()  #返回的是所有能在该函数里访问的命名
print "------------------------------------------------------------------"
reload(addutils.modeltest)