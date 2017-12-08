#!/usr/bin/env python
#-*-coding:utf-8-*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')

s="a中国人\tb中国人\tc中国人\td中国人.yes"
print s.capitalize();#首字母大写
print s.center(70) #多少个宽度居中
print s.count('a',0,5)
print s.decode("utf-8", 'ignore' )
print s.encode("utf-8", 'ignore' )
print s.endswith("yes")
print s.expandtabs(8)
print s.find('a',0,1),s.find('c',8)
print len(s)
print s.isalnum(),"sbs233".isalnum()  #所有的都是字符串或者数字组合
print "ffdfdfs".isalpha(),"3434".isalpha() #判断所有的是否是字符串
print u"222".isdecimal(),u"0b11".isdecimal()#是否只包含10进制数据
print u"34".isnumeric() #只包含数字字符
print "34343".isdigit()#只包含数字
print "dddD".islower(),"dd".islower()
print " ".isspace()
print "Im Is Good Boy".istitle(),"im IS Good Boy".istitle() #如果字符串中所有的单词拼写首字母是否为大写，且其他字母为小写则返回 True，否则返回 False.
print "IM".isupper() #全为大写
print "-".join("3454545effdfdf")
print "wjs".ljust(30),4
print "WJS".lower()
print "  wjs  ".lstrip(),","
print "  wjs  ".rstrip(),","
from string import maketrans
result=maketrans("wjs","124")
print "wjs haha wo qu".translate(result)#将w换成1 j换成2 s换成4
print max("wjs")
print min("wjs")
rs="wjs,ha,wo,dos,so,ddd".partition(",")
print "wjs,ha,wo,dos,so,ddd".rpartition(",")
print "-----------"
for x in rs:
    print x
print "2r r rer".replace("r","2",1)
print "wjswjswjswjswjs".rfind("wjs",3,6)
print "jsjdaidlasdiw".rindex("d",1,4)
print "wjs".rjust(40),5
print "wjs,wjs,wjs,wjs".split(",",1)
print "ww\ndfdf\r\ndfdfd\r".splitlines(),"ww\ndfdf\r\ndfdfd\r".splitlines(True)
print "wjs.sjs.sj".startswith('wjs'),"wjs.sjs.sj".startswith('.',3,7)
print "wjs.wjs.config.exe".endswith('exe'),"wjs.wjs.config.exe".endswith("config",8,14)
print "    wjs   ".strip(),'end'
print "wjs".zfill(40)
print u"3434354534".isdecimal()

