#!/usr/bin/env python
# coding:utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender="w_wangjiawei@hfbank.com.cn"
receivers=['w_wangjiawei@hfbank.com.cn']

server="mail.hfbank.com.cn"
port="25"

mailmessage="""
<p>邮件发送的内容哈哈</p>
<p><a href='http://www.baidu.com'>百度 </a></p>
"""
message=MIMEText(mailmessage,'html','utf-8')
message['From']=Header("王家胜发送",'utf-8')
message['To']=Header("王家胜接受",'utf-8')
message['Subject']=Header("邮件的标题",'utf-8')

try:
    print 1
    smtpObj=smtplib.SMTP(server,port)
    print 2
    smtpObj.starttls()
    smtpObj.login(sender,"Wang812330500")
    print 3
    smtpObj.sendmail(sender,receivers,message.as_string());
    print 4
    print "邮件发送成功"
except smtplib.SMTPException,mesobj:
    print "邮件发送失败:"+mesobj