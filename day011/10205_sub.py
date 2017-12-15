#!/usr/bin/env python
# coding:utf-8
import re
phone = "2004-959-559 #这个需要删除"
# 删除字符串中的 Python注释
num=re.sub(r'#.*$',"",phone)
print "电话号码是:",num
#\D删除字符串中的非数字
num=re.sub(r"\D","",phone)
print "电话号码是:",num
