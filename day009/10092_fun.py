#!/usr/bin/env python
# coding:utf-8
class A(object):
    def __init__(self):
        self.wocao="i\`m the parent"
        print('Parent')
    def bar(self,message):
        print("%s from Parent" %message)
class FooChild(A):
    def __init__(self):
        super(FooChild, self).__init__()
        print ('Child')
    def bar(self,message):
        super(FooChild,self).bar(message)
        print "Child bar function"
        print self.wocao
if __name__=='__main__':
    fooChild =FooChild()
    fooChild.bar("HelloWorld")