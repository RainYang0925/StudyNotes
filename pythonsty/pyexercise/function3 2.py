#!/usr/bin/env python
#-*- coding: utf-8

#函数属性,函数是对象也有属性
def cang():
    '''This is function of changlaoshi'''
    pass

#变量／参数／形参／实参
def add(x):             # x 是形参
    a = 10              # a 是变量
    return a + x        # x 是形参，本质是要传递赋给这个函数的值

def foo(lst):
    lst.append(99)
    return lst

if __name__ == "__main__":

    #函数文档查看
    lis = cang.__doc__
    print lis

    #增加函数属性
    breast = cang.breast = 90
    print breast

    print dir(cang)

    x = 3               # x 是变量
    print add(x)

    y = [1, 3, 5]
    print foo(y)

    print id(y)






