#!/usr/bin/env python2
# coding:utf-8
import MySQLdb
db=MySQLdb.connect("192.168.43.250","root","812330500","mysql");
cursor=db.cursor()
cursor.execute("select version()")
data=cursor.fetchone();
print "Database version:%s" % data