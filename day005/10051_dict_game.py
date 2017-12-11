#!/usr/bin/env python
#-*-coding:utf-8-*-
dictionary={}
flag="a"
forflag="a"
while flag=='a' or flag=="c":
    print "添加 查找单词或者退出a/c/e"
    flag=str(raw_input())
    if(flag=='a'):
        print "请输入key值:"
        ikey=raw_input()
        print "请输入value值"
        ivalue=raw_input()
        dictionary.setdefault(ikey,ivalue)
        print "是否显示dictionary y/n"
        inputdata=raw_input()
        if inputdata=="y":
            print dictionary
        else:
            continue
    elif(flag=='c'):
        print "请输入你要查找的词"
        istr=raw_input()
        for itatorvalue in sorted(dictionary.keys()):
            if(istr==itatorvalue):
                print "发现Value",dictionary[itatorvalue]
                forflag='a'
                break
            else:
                forflag="b"
        if(forflag=="b"):
            print "没有找到"
    elif flag=="e":
        break
    else:
        print "error inpout"