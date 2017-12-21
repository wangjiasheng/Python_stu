#!/usr/bin/env python
# coding:utf-8
import MySQLdb;
db=MySQLdb.connect("192.168.43.250","root","812330500","User");
sql2="insert into User(name,lastname,age,sex,Income)values('wjs','jiasheng',14,'1',1.5);"
cursor=db.cursor();
try:
    data=cursor.execute(sql2);
    db.commit();
    print data
except:
    db.rollback();
db.close();