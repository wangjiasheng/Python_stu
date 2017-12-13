#!/usr/bin/env python
# coding:utf-8
try:
    pass
finally:
    print "try 1 执行结束"
try:
    raise IOError("文件发生异常，哈哈")
    pass
except IOError:
    print "try 2发生了异常"
finally:
    print "try 2执行结束"
try:
    raise IOError("文件发生异常，try3")
    pass
finally:
    print "try 3 执行结束"