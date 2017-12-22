#!/usr/bin/python
# coding:utf-8
import socket
s=socket.socket()
host=socket.gethostname()
prot = 8012
s.connect((host,prot))
print s.recv(1024)
s.close()