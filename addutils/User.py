#!/usr/bin/env python
# coding:utf-8
class User:
    '卧槽'
    x=100;
    @property
    def getUsername(self):
        return self.x;
    @getUsername.setter
    def setUsername(self,username):
        self.x=username
    @getUsername.deleter
    def deleteUsername(self):
        del self.x