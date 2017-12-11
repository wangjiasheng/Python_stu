#!/usr/bin/env python
#-*-coding:utf-8-*-
dict1={"name":"wjs","age":27,"sex":"男"}
print dict1['name']
dict1['name']="wangjiasheng"
print dict1['name']
del dict1['sex']
print dict1
dict1.clear()
print dict1
#ditc特性
dict2={"name":"wjs","name":"wangjiasheng"}#只能记住一个
print dict2
#字典内置函数
print cmp(dict1,dict2)
print len(dict2)
print str(dict2)
print type(dict2)
#字典的函数
dict1.clear()
dict3=dict2.copy()
print id(dict1),id(dict2)
print "-----------fromkeys------------"
seq=["wjs","jia","sheng"]
print dict.fromkeys(seq)
print dict.fromkeys(seq,"未知")
print dict2.get("name") #Get
print dict2.has_key("name")#haskey
print dict2.items()
print dict2.keys()
print dict2.setdefault("name",None)
print dict2.setdefault("haha","淘宝")
print dict2
print dict1,dict2
dict1.setdefault("badmen","wjs")
dict1.update(dict2)
print dict1
print dict1.pop("badmen")
print dict1.popitem()
print dict1
for x in dict1:
    print x
for x in dict1.keys():
    print x
print dict1.keys()
print sorted(dict1)