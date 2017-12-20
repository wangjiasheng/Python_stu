#!/usr/bin/env python2
# coding:utf-8
print "Content-Disposition:attachment;filename=\"foo.txt\""
print
print """
<html>
    <head>
        <meta charset='utf-8'>
        <head>头部信息</head>
    </head>
    <body>
"""
fos=open("/tmp/ffmpeg.txt","rb");
strs=fos.read()
print str
fos.flush();
fos.close();
"""
    </body>
</html>
"""