#!/usr/bin/env python2
# coding:utf-8
import thread
import time;
def print_time(threaName,delay):
    count = 0;
    while count <5:
        time.sleep(delay)
        count+=1
        print "%s:%s" % (threaName,time.ctime(time.time()))
try:
    thread.start_new_thread(print_time,("线程1",0.1));
    print "哈哈"
    thread.start_new_thread(print_time,("线程2",0.1));
except Exception,message:
    print "Error",message
while 1:
    pass