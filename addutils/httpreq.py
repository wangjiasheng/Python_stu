#!/usr/bin/env python
# coding:utf-8
import httplib;
import urllib;
httpcon=httplib.HTTPConnection("api.k780.com")
params=urllib.urlencode({"app":"weather.future","weaid":"1","appkey":"10003","sign":"b59bc3ef6191eb9f747dd4e83c99f2a4","format":"json"})
headers={"Content-type":"application/x-www-form-urlencoded","Accept":"text/json"}
req=httpcon.request("POST","/",params,headers)
rep= httpcon.getresponse()
print rep.status ,rep.reason
print rep.read()