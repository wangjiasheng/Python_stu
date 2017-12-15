#!/usr/bin/env python
# coding:utf-8
import re
'''
.* 第一个匹配分组，.* 代表匹配除换行符之外的所有字符。
.*?第二个匹配分组，.*? 后面多个问号，代表非贪婪模式，也就是说只匹配符合条件的最少字
'''
line = "Cast are smarter than dogs"
matchObj=re.match(r"(.*) are (.*?) .*",line,re.M|re.I)
if matchObj:
    print matchObj.group()
    print matchObj.group(1)
    print matchObj.group(2)