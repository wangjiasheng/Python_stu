#!/usr/bin/env python
# coding:utf-8
class A:
    def foo(self):
        print "called A.foo()"
class B:
    pass
class C:
    def foo(self):
        print("called C.foo")
class D(B,C):
    pass
if __name__ == '__main__':
    d=D()
    d.foo()