#!/usr/bin/env python
# coding:utf-8
import addutils.MySQLDB
import MySQLdb
dbinfo=addutils.MySQLDB
conn=MySQLdb.connect(dbinfo.dbhost,dbinfo.dbuser,dbinfo.dbpasswd,dbinfo.dbname)
cursor=conn.cursor()
sql="update User set name='wjs',lastname='jiasheng',age=14,sex='N',Income=1.3 WHERE sex = '%c'" % '�'
try:
    cursor.execute(sql)
    conn.commit()
except:
    print "Error"
    conn.rollback()
conn.close()