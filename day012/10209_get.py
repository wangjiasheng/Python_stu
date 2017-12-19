#!/usr/bin/env python2
# coding:utf-8
import cgi,cgitb
form=cgi.FieldStorage();
username=form.getvalue("username");
passwrod=form.getvalue("password");
print "Content-type:text/html"
print
print "<html>"
print "<head>"
print "<meta charset='utf-8'>"
print "<title>菜鸟教程</title>"
print "</head>"
print "<body>"
print "<h2>%s官网:%s</h2>"(username,passwrod)
print "</body>"
print "</html>"