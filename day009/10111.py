#!/usr/bin/env python
# coding:utf-8
x = 10
expr = """
z = 30
sum = x + y + z
print(sum)
"""


def func():
    y = 20
    exec (expr)
    exec (expr, {'x': 1, 'y': 2})
    exec (expr, {'x': 1, 'y': 2}, {'y':8, 'z': 4})
func()