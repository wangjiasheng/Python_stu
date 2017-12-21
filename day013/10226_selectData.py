#!/usr/bin/env python
# coding:utf-8
import MySQLdb;
import addutils.MySQLDB
db=addutils.MySQLDB
conn=MySQLdb.connect(db.dbhost,db.dbuser,db.dbpasswd,db.dbname)
cousro=conn.cursor()
sql="select * from User WHERE age>%d" % 1
try:
    result=cousro.execute(sql)
    data=cousro.fetchall()
    for x in data:
        name=x[0]
        lastname=x[1]
        age=x[2]
        sex=x[3]
        ints=x[4]
        print 'name=%s,lastname=%s,age=%d,sex=%c,float=%f' % (name,lastname,age,sex,ints)
except:
    print "ERROR";
    conn.rollback()
conn.close();