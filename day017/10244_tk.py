#!/usr/bin/env python
# coding:utf-8
from Tkinter import *
root=Tk()
li=['c','python','php','html','SQL','java']
movie=['CSS','JQuery','Bootstrap']
listb=Listbox(root)
listb2=Listbox(root)
for item in li:
    listb.insert(0,item)
for item in movie:
    listb2.insert(0,item)
listb.pack()
listb2.pack()
root.mainloop()