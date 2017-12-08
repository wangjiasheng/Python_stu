#!/usr/bin/env python
#-*-coding:utf-8-*-
tuple=('我操',"你妈",'haha',"ahaha",666)
tinytuple=('我去',"不是吧","阿西吧")
print(tuple)
print tuple[0]
print tuple[1:3]
print tuple[2:]
print tinytuple * 2
print tuple+tinytuple

list=list(tuple); #强制转换产生了新对象
list[0]=200
list[1]=200
list[2]=200
list[3]=200
print("强制转换前")
print tuple
print("强制转换后")
print list
