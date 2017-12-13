#!/usr/bin/env python
#coding:utf-8
print bin(3)

fs=file("d:/1.txt","w");
fs.write("哈哈")
fs.flush();
fs.close();
fc=file("d:/1.txt","r");
print fc.read()
fc.close()

listv=[1,2,3,5,7,8,9,9,0,5,3,5,3]
for i in iter(listv):
    print i
