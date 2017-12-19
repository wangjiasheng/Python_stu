#!/usr/bin/env python
# coding:utf-8
import httplib
import time
import json
import urllib2
import cookielib
headers={
    'Content-Type':'application/json',
    'Accept':'*/*',
    'Date':time.strftime("%a, %d %b %Y %H:%M:%S GMT",time.localtime(time.time())),
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6',
    'Host': 'map.baidu.com',
    'Proxy - Connection': 'keep - alive',
    'Referer': 'http: // map.baidu.com /',
    'Cookie':'BIDUPSID=7C7483A04C333D368CA5C47BDA16C7B0; PSTM=1502329011; BDUSS=3ZSU0p5akt2VXEwU1dTMzlWSU1mU1F0T0dpRjRFelFUS2hXR08ySlhuQVFHTXRaSVFBQUFBJCQAAAAAAAAAAAEAAAA06qkdMzE0MjMyMzMyAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABCLo1kQi6NZZ; __cfduid=d84e1f1d15aaa0f9e0ccc3742c260f0351506683582; BAIDUID=6B82B709B0D55B639CBF40A1E7514DE2:FG=1; locale=zh; BCLID=11653679064779134988; BDSFRCVID=sOFsJeC62mum1j6A-oNQei1g62DfhvnTH6ao5EFdVutLwUfqPtxgEG0PqM8g0Ku-abvWogKK0mOTHUrP; H_BDCLCKID_SF=JRPHoI--JKvbfP0khtn_2JLHqxbXqMr8X57Z0l8KtDbjDK3GKxLVhp0bbfuDK5KHaC6--IOmWIQHDPoyXj0MWb_7KtobX4380mO4KKJx3nLWeIJo5DciMTDrhUJiB5OLBan7-4oxfD_MhC-wjT8Men-W5gT3a4b3bK68sJOOa6rjDCvd-fr5y4LdjG5xQfczyHnCsR7m5n5EhJ0CDxR1yTDX3-Aq54Rj-Rvp_fI-tJciqPFCL4tWQfbQ0-OuqP-jW5TaBpu-bb7JOpkxhfnxyhLX0aCqtTtjfRujV-35b5rEMjrnhPF_-P6MbnnTbMT-0bFHWUQoWlP5Ej6vbPcqMj_sjG5L54Qntan7_JjOJ4bj84cL3xcT5hbDDRrfhUQxtNRDXInjtpvhKJj2KJ3obUPUDMc9LUvP-H4E_D8yJIK2hDv65nt_2JLH5MnXKbvtato2WbCQ-h7PqpcNLTDKhJLDDfCq3CryBH6-BCjjJDoUeRnChlO1j4_ejtolKp5tbgJf-RQhLPbWep5jDh3aXjksD-Rte4oabHvy0hvctn6cShnaKl00-nDSHH8Ot50e3J; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; PSINO=1; H_PS_PSSID=1463_21083_17001_20881_25178_22158; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; M_LG_UID=497674804; M_LG_SALT=e6e888d6b9f817023b9c27c23efeee0c; validate=28744; MCITY=-131%3A',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'
}
params=""
#请求网络
conn=httplib.HTTPConnection("map.baidu.com")
req=conn.request("GET","/v&t=1513217614771",params,headers)
rep=conn.getresponse()
print rep.status,rep.reason
result=rep.read()
#JSON解析
jsonobj= json.loads(result)
captcha_err_no=jsonobj['captcha_err_no']
captcha_str_reason=jsonobj['captcha_str_reason']
captcha_vcode_str=jsonobj['captcha_vcode_str']
#保存Cookie
cookie=cookielib.CookieJar();
handler=urllib2.HTTPCookieProcessor(cookie);
opener=urllib2.build_opener(handler)
opener.open("http://map.baidu.com")
name=""
value=""
for item in cookie:
  name=item.name
  value=item.value
#请求网络
smsheaders={
    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept':'*/*',
    'Set-Cookie':'BIDUPSID=7C7483A04C333D368CA5C47BDA16C7B0; PSTM=1502329011; BDUSS=3ZSU0p5akt2VXEwU1dTMzlWSU1mU1F0T0dpRjRFelFUS2hXR08ySlhuQVFHTXRaSVFBQUFBJCQAAAAAAAAAAAEAAAA06qkdMzE0MjMyMzMyAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABCLo1kQi6NZZ; __cfduid=d84e1f1d15aaa0f9e0ccc3742c260f0351506683582; '+name+'='+value+'; locale=zh; BCLID=11653679064779134988; BDSFRCVID=sOFsJeC62mum1j6A-oNQei1g62DfhvnTH6ao5EFdVutLwUfqPtxgEG0PqM8g0Ku-abvWogKK0mOTHUrP; H_BDCLCKID_SF=JRPHoI--JKvbfP0khtn_2JLHqxbXqMr8X57Z0l8KtDbjDK3GKxLVhp0bbfuDK5KHaC6--IOmWIQHDPoyXj0MWb_7KtobX4380mO4KKJx3nLWeIJo5DciMTDrhUJiB5OLBan7-4oxfD_MhC-wjT8Men-W5gT3a4b3bK68sJOOa6rjDCvd-fr5y4LdjG5xQfczyHnCsR7m5n5EhJ0CDxR1yTDX3-Aq54Rj-Rvp_fI-tJciqPFCL4tWQfbQ0-OuqP-jW5TaBpu-bb7JOpkxhfnxyhLX0aCqtTtjfRujV-35b5rEMjrnhPF_-P6MbnnTbMT-0bFHWUQoWlP5Ej6vbPcqMj_sjG5L54Qntan7_JjOJ4bj84cL3xcT5hbDDRrfhUQxtNRDXInjtpvhKJj2KJ3obUPUDMc9LUvP-H4E_D8yJIK2hDv65nt_2JLH5MnXKbvtato2WbCQ-h7PqpcNLTDKhJLDDfCq3CryBH6-BCjjJDoUeRnChlO1j4_ejtolKp5tbgJf-RQhLPbWep5jDh3aXjksD-Rte4oabHvy0hvctn6cShnaKl00-nDSHH8Ot50e3J; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; PSINO=1; H_PS_PSSID=1463_21083_17001_20881_25178_22158; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; M_LG_UID=497674804; M_LG_SALT=e6e888d6b9f817023b9c27c23efeee0c; validate=28744; MCITY=-131%3A',
    'Date':time.strftime("%a, %d %b %Y %H:%M:%S GMT",time.localtime(time.time())),
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
    'Host':'map.baidu.com',
    'Origin':'http://map.baidu.com',
    'Proxy-Connection':'keep-alive',
    'Referer':'http://map.baidu.com/',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'
}
print captcha_vcode_str
smsparams="newmap=1&s=inf%26uid%3Dd5d7606d8c02ae5128201a76%26c%3D131%26newmap%3D1%26it%3D1"
connsms=httplib.HTTPConnection("map.baidu.com")
smsreq=connsms.request("POST","/ag/sms/sendnew/",smsparams,smsheaders)
smsrep=connsms.getresponse()
print smsrep.status,smsrep.reason
result=smsrep.read()
print result



