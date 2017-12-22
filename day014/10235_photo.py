#!/usr/bin/env python
# coding:utf-8
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header

sender="w_wangjiawei@hfbank.com.cn"
pwssword="Wang812330500"

receivers=['w_wangjiawei@hfbank.com.cn']

server="mail.hfbank.com.cn"
port="25"

filepart=MIMEMultipart('related')
filepart['From']=Header('王家胜发送','utf-8');
filepart['To']=Header('王家胜接受','utf-8');
filepart['Subject']=Header('主题','utf-8');

msgpart=MIMEMultipart('alternative')                                    #可以添加多个附件
filepart.attach(msgpart)                                                  #filepart放入MIMEMultipart的所有附件

mail_msg="""
<p>邮件发送测试</p>
<p><a href="http://www.runoob.com">百度</a></p>
<p><img src="cid:image1"></p>
"""
msgpart.attach(MIMEText(mail_msg,'html','utf-8'))                       #放入一个网页附件


fp=open("e:/test.jpg",'rb')
msgImg=MIMEImage(fp.read())
fp.close()
msgImg.add_header('Content-ID','<image1>')
filepart.attach(msgImg);                                                  #filepart放入图片附件
try:
    smtpObj=smtplib.SMTP(host=server,port=port)
    smtpObj.starttls()
    smtpObj.login(user=sender,password=pwssword)
    smtpObj.sendmail(sender,receivers,filepart.as_string())
    print "SEND Sucess"
except smtplib.SMTPException:
    print "ERROR"