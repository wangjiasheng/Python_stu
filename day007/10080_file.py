#!/usr/bin/env python
# coding:utf-8
fo=open("d:/1.txt","w+")
list1=[]
for x in range(0,100):
    fo.write("卧槽"+str(x)+"\r\n")
fo.flush()
print "文件的描符",fo.fileno()
print fo.isatty()  #文件上是否连接到一个终端
fo.close()
print "-----------read------------"
fs=open("d:/1.txt","r+")
print fs.readline(),fs.next()
fs.close()
print "------------readline-------------"
fc=open("d:/1.txt","r+")
print fc.readlines(2)
fc.close()
print "---------------truncate----------------"
fg=open("d:/1.txt","r+")
print fg.readline()
fg.truncate(30)
listsub= fg.readlines()
print listsub
print listsub[0]
print listsub[1]