#!/usr/bin/env python
# coding:utf-8
import MySQLdb
import addutils.MySQLDB
dbsetup=addutils.MySQLDB
conn=MySQLdb.connect(dbsetup.dbhost,dbsetup.dbuser,dbsetup.dbpasswd,dbsetup.dbname)
cursor=conn.cursor()
try:
    cursor.execute("delete from User where age =14")
    conn.commit()
except:
    print "Error"
    conn.rollback()
conn.close()