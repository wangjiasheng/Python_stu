#!/usr/bin/env python
# coding:utf-8
fo =open("d:/1.txt","w+");
fo.write("我去你这个傻逼哈哈")
fo.close();

fs=open("d:/1.txt","r");
print fs.read(6);
print fs.tell();
fs.seek(6)
print fs.read()
fs.close()