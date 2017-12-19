#!/usr/bin/env python
# coding:utf-8
requestParams={
    "access_id":"434344",
    "Param":"Value",
    "timestamp":"565645",
    "message":"{\"title\":\"title\",\"content\":\"allmessage\"}",
    "message_type":"1"
}
print sorted(requestParams,lambda x,y:cmp(x,y))
