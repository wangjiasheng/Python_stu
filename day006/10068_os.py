#!/usr/bin/env python
# coding:utf-8
import os
print os.environ
print os.environ["PATH"]

path = os.getcwd()
os.chdir("C://")#改变当前目录
print os.getcwd()#获取当前目录
os.chdir(path)
print os.getcwd()

def printcomponent():
    print "组件的ID",os.getegid()
    print "用户的ID",os.getuid()
    print os.setgid()
    print os.setuid()
    print os.getgruops()  # 得到用户组名称列表
    print os.getlogin()  # 得到用户登录名称
    print os.getenv  # 得到环境变量
    print os.putenv  # 设置环境变量
    print os.umask  # 设置umask
#printcomponent()
print "-------------------------"

print os.system("dir") #利用系统调用，运行cmd命令