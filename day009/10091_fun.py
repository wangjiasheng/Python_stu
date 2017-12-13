#!usr/bin/env python
# coding:utf-8
print abs(-1) ,abs(1) #绝对值
print divmod(5,2)     #除法
# print input("请输入") #必须输入表达式   如输入134 打印 123 输入"哈哈" 打印 哈哈 输入哈哈(没有引号) 输出 报错 相当于eval(input())
# print raw_input("请输入:") #输入一却都返回字符串
# print open("d:/1.txt","w+").write("haha")
class E:
    @staticmethod
    def println():
        return "收到了"
class F(E):
    pass
print E.println()
print F.println()
print F().println()

print all([1,2,3,4,5,6]) #全部 不为0 不为"" 不为 False 不为 None 的python2.5上使用返回true
print "-----------------------any-----------------------"
print any([0,5,4,3,5,7,8,9,5])#全部为0 全部为"" 全部为Flase 全部为None 返回false
listv= [1,2,3,4,6,7,8,9,0,6,4,3,2,4,6,0,2,5,7]
s= enumerate(listv)
print len(listv)
for x,i in s:
    print x,i
print int("2")
print str(2)
print ord("a")
print eval("[2,3,4,5,6,8,9]")

class A:
    pass
class B(A):
    pass
print isinstance(A(),A),isinstance(B(),A)
print type(B()) == A ,type(B())==A

print pow(2,3)

print sum([1,2,3,4,5,6,7,8,9,8])

print isinstance("wocao",str)
print isinstance("wocao",unicode)
print isinstance("wocao",basestring) #是str和unicode的父类

execfile("C:/Users/wjs/PycharmProjects/untitled/addutils/printhelloword.py")
print issubclass(B,A)
print "我操了个"
