#!/usr/bin/env python
#coding:utf-8
def set_globvar_to_one():
    global globvar
    globvar =2
def print_globvar():
    print "hs",globvar
set_globvar_to_one()
print "wm",globvar
print_globvar();