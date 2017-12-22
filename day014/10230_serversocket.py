#!/usr/bin/env python
# coding:utf-8
import socket
s=socket.socket()
host=socket.gethostname()
prot=8012
s.bind((host,prot))
s.listen(5)
while True:
    c,addr=s.accept()
    print "连接地址",addr
    c.send("欢迎来到菜鸟")
    c.close();