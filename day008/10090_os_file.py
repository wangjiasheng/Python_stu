#!/usr/bin/env python
# coding:utf-8
import os;
print os.access("C:/Windows",os.F_OK)#测试文件是否存在
print os.access("C:/Windows",os.W_OK)#测试文件是否可写
print os.access("C:/Windows",os.R_OK)#测试文件是否可读
print os.access("C:/Windows",os.X_OK)#测试文件是否可跑
