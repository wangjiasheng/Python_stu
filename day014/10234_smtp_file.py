#!/usr/bin/env python2
# coding:utf-8
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

sender="w_wangjiawei@hfbank.com.cn"
pwssword="Wang812330500"

receivers=['w_wangjiawei@hfbank.com.cn']

server="mail.hfbank.com.cn"
port="25"

message=MIMEMultipart()
message['From'] = Header("王家胜发送","utf-8")
message['To'] = Header("王家胜接受","utf-8")
message['Subject'] = Header("邮件标题","utf-8")
message.attach(MIMEText("邮件内容","plain","utf-8"))

att1=MIMEText(open("C:/Users/wjs/PycharmProjects/untitled/README.md").read(),"base64",'utf-8')
att1['Content-Type']='application/octet-stream'
att1['Content-Disposition']='attachment;filename="text.txt"'
message.attach(att1);

att2=MIMEText(open("C:/Users/wjs/PycharmProjects/untitled/README.md").read(),"base64",'utf-8')
att2['Content-Type']='application/octet-stream'
att2['Content-Disposition']='attachment;filename="text.txt"'
message.attach(att2);

try:
    smtpObj=smtplib.SMTP(server,port);
    smtpObj.starttls();
    smtpObj.login(sender,pwssword);
    smtpObj.sendmail(sender,receivers,message.as_string());
    print "邮件发送成功"
except smtplib.SMTPException:
    print "发送失败"