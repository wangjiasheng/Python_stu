#!/usr/bin/env python2
# coding:utf-8
import Queue
import threading
import time
exitFlag=0
class myThread(threading.Thread):
    def __init__(self,threadID,name,q):
        threading.Thread.__init__(self)
        self.threadID=threadID
        self.name=name
        self.q=q
    def run(self):
        print "Starting "+self.name
        process_data(self.name,self.q)
        print "Exiting "+self.name
def process_data(name,q):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data=q.get()
            queueLock.release()
            print "%s processing %s" % (name,data)
        else:
            queueLock.release()
        time.sleep(1)
threadList=["Thread-1","Thread-2","Thread-3","Thread-4","Thread-5","Thread-6","Thread-7","Thread-8","Thread-9","Thread-10","Thread-11","Thread-12","Thread-13","Thread-14","Thread-15"]
nameList=["One","Two","Three","Four","Five"]
queueLock=threading.Lock()
workQueue=Queue.Queue(16)
threads=[]
threadID=1
#创建队列线程
for tName in threadList:
     thread = myThread(threadID,tName,workQueue)
     thread.start()
     threads.append(thread)
     threadID+=1
#填充队列
queueLock.acquire()
for word in threadList:
    workQueue.put(word)
queueLock.release()

#等待队列清空
while not workQueue.empty():
    pass
#通知线程退出
exitFlag=1
#等待所有线程完成
for t in threads:
    t.join()
print "Exiting Main Thread"
