#!/usr/bin/env python
#-*-coding:utf-8-*-
import math;
import random
list=[1,5,8]
print random.choice(list)
print random.randrange(4,20,2)
print random.random()
#suffle
random.shuffle(list)
print list
random.shuffle(list)
print list
#suffle
print random.uniform(0,5)
print random.randint(2,7)