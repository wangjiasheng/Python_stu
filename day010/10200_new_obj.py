#!/usr/bin/env python
# coding:utf-8
class A:
    def foo(self):
        print "called A.foo()"
class B(A):
    pass
class C(A):
    def foo(self):
        print("called C.foo")
class D(A):
    def foo(self):
        print("called D.foo")
class E(B,D,C,object): #没有object 继承从左到右，有object 同父类从左到右 否则继承辈分最小的
    pass
if __name__ == '__main__':
    d=E()
    d.foo()