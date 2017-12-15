#!/usr/bin/env python
# coding:utf-8
import re
print re.search("www","www.baidu.com").span()
print re.search("com","www.baidu.com").span()