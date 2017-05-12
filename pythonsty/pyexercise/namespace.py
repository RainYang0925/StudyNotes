#!/usr/bin/env python
# coding=utf-8

#全局变量／局部变量
'''
在Python程序中，变量的作用域是有在函数、类中才能被改变
如果不是在函数或者类中，比如在循环或者条件语句中，变量都是在同一层级的作用域中
'''

x = 2           #全局变量

def funcx():
    x = 9       #局部变量，只在函数体内起作用
    print "this x is in the of funcx:-->", x

# global
def func1x():
    global x    #申明x为一个全局变量
    x = 9
    print "this x is in the of funcx:-->", x

def outer_foo():
    a = 10
    def inner_foo():
        a = 20
        print "inner_foo,a=", a      #a=20
                                                           #Python 3的读者，请自行修改为print()函数形式，下同，从略
    inner_foo()
    print "outer_foo,a=", a          #a=10

a = 30

#命名空间


if __name__ == "__main__":

    print funcx()
    print func1x()
    print "------------------------------"
    print "this x is out of funcx:-->", x

    print "------------foo()--------------"
    print outer_foo()
    print "a=", a