#!/usr/bin/python
# coding:utf-8
import re
def double(matched):
    return str(int(matched.group("value"))*2);
s='Q23G34a88d20R45'
ma=re.sub('(?P<value>\d+)',double,s)
print s,ma