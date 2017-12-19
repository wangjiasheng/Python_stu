#!/usr/bin/env python
# coding:utf-8
import httplib
import time
import hashlib
ACCESS_ID="2100238242"
time=int(round(time.time()*1000)/1000)
ACCESS_KEY="A1HKJ5883SGM"
ACCESS_SECRET="d497c3b220183d047ee691646d2bd32c" #65a6c9837a92c92b8a087a8406cad269
REQUESTMETHOD="GET"
URL="openapi.xg.qq.com"
ACTION="/v2/push/all_device"
requestParams={
    "access_id":ACCESS_ID,
    "timestamp":str(time),
    "message":"{\"title\":\"title\",\"content\":\"allmessage\"}",
    "message_type":"1",
}
keysort= sorted(requestParams,cmp=lambda x,y:cmp(x,y))              #参数排序
def addStr():
    STRSIGN = ""
    for key in keysort:  # 拼接排序后参数
        STRSIGN = STRSIGN + key + "=" + requestParams[key]
    return STRSIGN
def addParam():
    str = ""
    for key in keysort:  # 拼接排序后参数
        str = str + key + "=" + requestParams[key] + "&"
    str = str[0:-1]
    return str;

STRSIGN= REQUESTMETHOD + URL + ACTION + addStr() +ACCESS_SECRET   #拼接请求参数
print "签名前的字符串:"+STRSIGN
sign=hashlib.md5(STRSIGN).hexdigest()                                    #计算sign
print "签名结果:"+sign
urlparams= addParam()+"&sign="+sign                                        #拼接sign
print "请求的参数:"+urlparams
reqheaders={
    'Content-type':'application/x-www-form-urlencoded',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Host':'www.renren.com',
    'Origin':'http://zhichang.renren.com',
    'Referer':'http://zhichang.renren.com',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1'
}
conn=httplib.HTTPConnection(URL)
request=conn.request(REQUESTMETHOD,ACTION,urlparams,reqheaders)
response=conn.getresponse()
print response.status,response.reason
print response.read()
