#!/usr/bin/env python
#-*-coding:utf-8-*-
import random
dict1={1:"石头",2:"剪刀",3:"布"}
dict2={"石头":1,"剪刀":2,"布":3}
dict3={-1,2}
dict4={1,-2}
while 1:
    inputstr = raw_input("请输入:")
    result = random.randint(1, 3)
    print "系统出:" + dict1.get(result)
    if(inputstr not in dict2):
        if(inputstr == "exit"): break
        else: print("不合法重新输入")
    else:
       selfinput= dict2.get(inputstr)
       if((selfinput-result) in dict3):
           print "系统出:"+dict1.get(result)+" 你出:"+inputstr+" 你输了!"
       elif ((selfinput - result) in dict4):
           print "系统出:" + dict1.get(result) + " 你出:" + inputstr + " 你输了!"
       elif(selfinput-result==0):
           print "系统出:" + dict1.get(result) + " 你出:" + inputstr + " 平局!"
       else:
           print "系统出:" + dict1.get(result) + " 你出:" + inputstr + " 未知!"