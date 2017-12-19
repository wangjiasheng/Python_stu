#!/usr/bin/env python2
# coding:utf-8
import cgi,cgitb
form =cgi.FieldStorage();
sexnan=form.getvalue("sex")
seletc=""
if sexnan=="nan":
    seletc="男"
elif sexnan=="nv":
    seletc=="女"
else:
    seletc="没有选择"
print "Content-Type:utf-8"
print
print "<html>"
print "<head>"
print "<meta charset='utf-8'>"
print '<title>我日</title>'
print "</head>"
print "<body>"
print "结果：%s" % seletc
print "</body>"
print "</html>"