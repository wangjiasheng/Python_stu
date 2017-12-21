#!/usr/bin/env python2
# coding:utf-8
import MySQLdb
import addutils.MySQLDB
connSet=addutils.MySQLDB
conn=MySQLdb.connect(connSet.dbhost,connSet.dbuser,connSet.dbpasswd,connSet.dbname)
cursor=conn.cursor();
try:
    cursor.execute("insert into User(name,lastname,age,sex,Income) values ('%s','%s',%d,'%c',%f);" %("wjs","jiasheng",10,"n",1.3))
    cursor.execute("insert into User(name,lastname,age,sex,Income) values ('%s','%s',%d,'%c',%f);" %("wjs","jiasheng",11,"n",1.3))
    cursor.execute("insert into User(name,lastname,age,sex,Income) values ('%s','%s',%d,'%c',%f);" %("wjs","jiasheng",12,"n",1.3))
    cursor.execute("insert into User(name,lastname,age,sex,Income) values ('%s','%s',%d,'%c',%f);" %("wjs","jiasheng",13,"n",1.3))
    cursor.execute("insert into User(name,lastname,age,sex,Income) values ('%s','%s',%d,'%c',%f);" %("wjs","jiasheng",14,"n",1.3))
    cursor.execute("insert into User(name,lastname,age,sex,Income) values ('%s','%s',%d,'%c',%f);" %("wjs","jiasheng",15,"n",1.3))
    cursor.execute("insert into User(name,lastname,age,sex,Income) values ('%s','%s',%d,'%c',%f);" %("wjs","jiasheng",16,"n",1.3))
    conn.commit()
    data=cursor.fetchall();
    for item in data:
        print item
except:
    print "error"
    conn.rollback()
conn.close()