#!/usr/bin/env python
#-*-coding:utf-8-*-
rows=4
blank=" "
draw="*"
for i in range(0, rows):
    for k in range(0, rows * 2 - 1):
        if((rows - i - 1 == k) or (rows + i - 1 == k))and(i!=rows-1):
            print draw,
        elif i==rows-1:
            if(k%2==0):
                print draw,
            else:
                print blank,
        else:
            print blank,
    print