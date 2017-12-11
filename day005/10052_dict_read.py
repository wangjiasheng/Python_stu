#!/usr/bin/env python
#-*-coding:utf-8-*-
users={
    'user1':{
        "username":"wjs",
        "userage":"38",
        "usersex":"男"
    },
    'user2':{
        "username":"wangju",
        "userage":"36",
        "usersex":"女"
    }
}
for user_x,userobj in users.items():
    print user_x
    print userobj