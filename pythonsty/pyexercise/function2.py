#!/usr/bin/env python
#coding: utf-8 -*-

# 定义函数,先定义后使用
def name():
    print "rainyang"

#函数没有return默认返回为None
def add_function(a, b):
    c = a + b
#   return c

def add(x, y):
    print "x=", x
    print "y=", y
    return x + y
#指定给函数传默认参数
def times(x, y = 2):
    print "x=", x
    print "y=", y
    return x*y

def bar():
    pass
#调用函数前必须先定义
def foo():
    print "hello, rain"
    bar()   #未定义函数

#返回值，函数向调用的地方返回数据
def fibs(n):
    result = [0, 1]
    for i in range(n-2):
        result.append(result[-2] + result[-1])
    return result
def my_fun():
    return 1, 2, 3



if __name__ == "__main__":
    result = add_function(2, 3)
    myname = add_function("rain","yang")

    print result
    print myname

    add(10, 3)
    add(y= 10, x= 3)

    times(3)
    times(3, 5)
    times("rainyang")

    foo()
    #返回一个值，返回一个列表
    lst = fibs(10)
    print lst
    #返回多个值，返回一个数组
    a = my_fun()
    print a

    x, y, z = my_fun()
    print x, y, z





