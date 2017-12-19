#!/usr/bin/env python2
# coding:utf-8
import os

print "Content-Type:text/html"
print
print "<meta charset='utf-8'>"
print "<b>环境变量</b>"
print "<ul>"
for key in os.environ.keys():
    print "<li><span tyle='color:green'>%30s</span>:%s</li>" %(key,os.environ[key])
print "</ul>"