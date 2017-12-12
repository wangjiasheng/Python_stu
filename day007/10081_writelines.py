#!/usr/bin/env python
# coding:utf-8
import os
fo=open("d:/1.txt","w+")
list1=[]
for x in range(1,100):
    list1.append("数据:"+str(x)+"\r\n")
fo.writelines(list1)
fo.flush()
fo.close()

fs=open("d:/1.txt","r")
list2 = fs.readlines();
for s in list2:
    print s;
print os.SEEK_SET