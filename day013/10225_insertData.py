#!/usr/bin/env python
# coding:utf-8
import MySQLdb;
db=MySQLdb.connect("192.168.43.250","root","812330500","User");
print "%c" % "c"
sql2="insert into User(name,lastname,age,sex,Income)values('%s','%s',%d,'%c',%f);" % ("wjs","jiasheng",10,'a',1.3)
cursor=db.cursor();
try:
    data=cursor.execute(sql2);
    db.commit();
    print data
except:
    db.rollback();
db.close();