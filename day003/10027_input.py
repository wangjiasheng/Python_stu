#!/usr/bin/env python
#-*-coding:utf-8-*-
import random
a=random.uniform(0,17);
print a
while(1>0):
    str = raw_input('请输入')
    if(str == "exit"):
        break
    if(str.isdigit()):
        print int(a)==int(str);
    else:
        print str;