#!/usr/bin/env python2
# coding:utf-8
import os;
import Cookie;
print "Content-type:text/html"
print
print """
<html>
    <head>
        <meta charset='utf-8'>
        <title>show Cookie</title>
    </head>
    <body>
    <h1>读取Cookies</h1>
"""
if 'HTTP_COOKIE' in os.environ:
    cookiestr=os.environ.get("HTTP_COOKIE");
    c=Cookie.SimpleCookie();
    c.load(cookiestr);
    try:
        data=c['name'].value;
        print "cookie data:"+data+"</br>"
    except KeyError:
        print "cookie没有设置或者已经过期"
print """
</body>
</html>
"""