#!/usr/bin/env python
# coding:utf-8
class A:
    x =1;
    def setUsername(self,username):
        self.username=username;
    def setPasswrod(self,password):
        self.passwrod=password;
    def getUserName(self):
        return self.username;
    def getPasswrod(self):
        return self.passwrod;
    def removeUserName(self):
        del self.username
    def removePasswrod(self):
        del self.passwrod
    property(getUserName,setUsername,removeUserName,"杉树")
    property(getPasswrod,setPasswrod,removePasswrod,"杉树")
a =A();
a.x=100;
a.username="wjs"
a.passwrod="812330500"

b =A();
b.x=200;
b.username="root"
b.passwrod="812330500"
class B:
    x=1;
    list1=[1,2,3,5]
print a.x,b.x
print a.username,b.username

c=B()
d=B()
d.list1=[2.3,5,6]
c.x=100;
d.x=200;
B.x=10;
print c.x
print d.x
print B.x
print c.list1,d.list1

listf=["username","passwrod","sex"]
for x in listf:
    print hasattr(b,x)