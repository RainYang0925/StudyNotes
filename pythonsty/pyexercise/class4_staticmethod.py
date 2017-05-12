#!/usr/bin/env python
#coding:utf-8

T = 1

def check_t():                  #类外面定义函数
    T = 3
    return T

class Foo(object):        #Python 3: class Foo:
    def __init__(self,name):
        self.name = name

    def get_name(self):
        if check_t():           #使用类外面定义的函数check_t()
            return self.name
        else:
            return "no person"

# @staticmethod                   #在类的作用域里面的时候，前面必须要加上一个装饰器@staticmethod,称之为静态方法
class Foo1(object):
    def __init__(self,name):
        self.name = name

    @staticmethod
    def check_t1():
        T = 1
        return T

    def get_name(self):
        if self.check_t1():
            return self.name
        else:
            return "no person"



if __name__ == "__main__":
    f = Foo("canglaoshi")
    name = f.get_name()
    print name        #Python 3: print(name)

    f1 = Foo1("canglaoshi")
    name = f1.get_name()
    print name