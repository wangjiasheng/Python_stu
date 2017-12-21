#!/usr/bin/env python
# coding:utf-8
import MySQLdb
db=MySQLdb.connect("192.168.43.250","root","812330500","User")
cursor=db.cursor()
cursor.execute("DROP TABLE IF EXISTS User;")
sql="create table User(name varchar(20),lastname varchar(20),age int,sex char(1),Income FLOAT);"
cursor.execute(sql)
db.close();