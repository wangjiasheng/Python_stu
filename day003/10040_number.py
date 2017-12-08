#!/usr/bin/env python
#-*-coding:utf-8-*-
a=1000
b="1000"
c = 10.4
d =5325
e =[2,3,4,5,7,4,3,6,7,3,5,7,4,2,7,3,4]
f=[4,5,6,2,6,2,8,3,9,5,3,6,8,5,3,6,8]
print type(int(b)),int(b)
print type(long(b)),long(b)
print type(float(b)),float(b)
print type(str(a)),str(a)
print type(complex(1,3)),complex(1,3)
print type(repr(e)),repr((e))
print type(eval("[2,3,5,6,4,3,6]")),eval("[2,3,5,6,4,3,6]")
print type(tuple(e)),tuple(e)
print type(list(tuple(e))),list(tuple(e))
print type(chr(96)),chr(97)
print type(unichr(97)),unichr(97)
print type(ord('A')),ord('A')
print hex(17)
print oct(9)