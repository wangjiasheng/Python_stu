#!/usr/bin/env python
#coding:utf-8
def reverse1(li):
    for i in range(0,len(li)/2):
        temp=li[i];
        li[i]=li[-i-1]
        li[-i-1]=temp
def reverse2(li):
    for i in range(0,len(li)/2):
        li[i],li[-i-1]=li[-i-1],li[i];
l=[1,2,3,4,5]
reverse2(l)
print l