#!/user/bin/env python
# coding:utf-8
import re
line = "Cast are smarter than dogs"
mat=re.match(r"dog",line,re.M|re.I)
if mat:
    print "match"
else:
    print "not match"
mat=re.search(r"dog",line,re.M|re.I)
if mat:
    print "search"
else:
    print "not search"