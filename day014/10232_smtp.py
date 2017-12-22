#/usr/bin/env python
# coding:utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header
"""
    http://mail.hfbank.com.cn
    w_wangjiawei@hfbank.com.cn
"""
sender="w_wangjiawei@hfbank.com.cn"
receivers=['w_wangjiawei@hfbank.com.cn']
server="mail.hfbank.com.cn"
port="25"

message=MIMEText('邮件的内容','plain','utf-8')
message['From']=Header("邮件发送者姓名",'utf-8')
message['To']=Header("邮箱接收者姓名",'utf-8')
message['Subject']=Header('邮件标题','utf-8')
try:
    print "1"
    smtpObj= smtplib.SMTP(server,port);
    print "2"
    smtpObj.starttls()
    print "3"
    s=smtpObj.login(sender,"Wang812330500")
    print "4",s
    smtpObj.sendmail(sender,receivers,message.as_string());
    print "邮件发送成功"
except smtplib.SMTPException,errm:
    print "ERROR无法发送:",errm