#!/usr/bin/env python2
# coding:utf-8
import cgi,cgitb
formdata=cgi.FieldStorage()
check1=formdata.getvalue("check1");
check2=formdata.getvalue("check2");
check1status='否'
check2status='否'
if check1:
    check1status='是'
else:
    check1status='否'
if check2:
    check2status='是'
else:
    check1status=='否'
print "ContentType:text/html"
print
print '<html>'
print '<meta charset="utf-8">'
print '<head>'
print '<title>'+'菜鸟哥哥'+'</title>'
print '</head>'
print '<body>'
print '<li>是否选中了：%s</li>' % check1status
print '<li>是否选中了：%s</li>' % check2status
print '</body>'
print '</html>'