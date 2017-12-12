#!/usr/bin/env python
# coding:utf-8
'''
    help(obj) #在线帮助, obj可是任何类型
    eval_r(str) # 表示合法的python表达式，返回这个表达式
'''
'''
    callable(obj) # 查看一个obj是不是可以像函数一样调用
    repr(obj) # 得到obj的表示字符串，可以利用这个字符串eval重建该对象的一个拷贝
    dir(obj)  #查看obj的name space中可见的name
    hasattr(obj,name) # 查看一个obj的name space中是否有name
    getattr(obj,name) # 得到一个obj的name space中的一个name
    setattr(obj,name,value)  #为一个obj的name
    #space中的一个name指向vale这个object
    delattr(obj,name) #从obj的name space中删除一个name
    vars(obj) #返回一个object的name space。用dictionary表示
    locals() #返回一个局部name space,用dictionary表示
    globals() #返回一个全局name space,用dictionary表示
    type(obj) #查看一个obj的类型
    isinstance(obj,cls) #查看obj是不是cls的instance
    issubclass(subcls,supcls) #查看subcls是不是supcls的子类
'''
print callable("")