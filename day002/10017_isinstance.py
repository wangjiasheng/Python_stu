#!/usr/bin/env python
#-*-coding:utf-8-*-
class A:
    pass
class B(A):
    pass
print isinstance(A(),A)
print isinstance(B(),A)
print type(A())==A,type(B())==B