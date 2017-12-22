#!/usr/bin/env python
# coding:utf-8
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

sender="314232332@qq.com"
pwssword="nlkptgkhgiwcbhhf"

receivers=['346382732@qq.com']

server="mail.hfbank.com.cn"
port="25"

def mail():
    ret=True
    try:
        msg=MIMEText('请一个一个删除','plain','utf-8');
        msg['From']=formataddr(["王家胜大王;王家胜大仙，王家胜上神",sender]);
        msg['To']=formataddr(["接收人;我就操了;忘记了",receivers]);
        msg['Subject']="中毒了";
        print 1
        server=smtplib.SMTP_SSL("smtp.qq.com",465)
        print 2,":",server
        loginres=server.login(sender,pwssword);
        print 3
        server.sendmail(sender,[receivers,],msg.as_string());
        print 4
        server.quit();
        print 5
    except Exception,excmsg:
        ret=False
        print excmsg
    return ret
for i in range(0,100):
    ret=mail();
    if ret:
        print "邮件发送成功"
    else:
        print "邮件发送失败"