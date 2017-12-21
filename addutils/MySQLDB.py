#!/usr/bin/env python2
# coding:utf-8
dbhost = "192.168.43.250";
dbuser = "root";
dbpasswd = "812330500";
dbname = "User";
class DBINFO:
    host=""
    user=""
    pasd=""
    dbnm=""
    def __init__(self):
        self.host="192.168.43.250";
        self.user="root";
        self.pasd="812330500";
        self.dbnm="User";
    def setHost(self,host):
        self.host=host;
    def getHost(self):
        return self.host;
    def delHost(self):
        del self.host;
    def setName(self,name):
        self.name=name;
    def getName(self):
        return self.name;
    def delName(self):
        del self.name;
    def getPassword(self):
        return self.name;
    def setPassword(self,pasd):
        self.pasd=pasd;
    def delPasd(self):
        del self.pasd;
    def setDBName(self,dbName):
        self.dbnm=dbName;
    def getDBName(self):
        return self.dbnm;
    def delDBName(self):
        del self.dbnm;
    property(setHost,getHost,delHost,"主机IP地址")
    property(setName,getName,delName,"数据库账户名称")
    property(setPassword,getPassword,delPasd,"数据库密码")
    property(setDBName,getDBName,delDBName,"数据库名称")