#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 多态--同一种行为具有不同表现形式和形态的能力，换一种说法，就是对象多种表现形式的体现。
print "this is a book".count('s')
print [1,2,4,3,5,3].count(3)

f = lambda x,y : x + y  # 参数类型无限制,不知道变量（参数）所引用的对象类型，也一样能进行操作
print f(2, 3)
print f("rain", "yang")
print f(["python","java"],["c++","lisp"])

# repr函数，针对输入的任何一个对象返回一个字符串
print repr([1,2,3])
print  repr({"lang":"python"})

def length(x):
    print "the length of ", repr(x),"is",len(x)

# 封装和私有化
# 封装(Encapsulation)是对具体对象的一种抽象，即将某些部分隐藏起来，在程序外部看不到，即无法调用
# “私有化”，就是将类或者函数中的某些属性限制在某个区域之内，外部无法调用。
class ProtectMe(object):
    def __init__(self):
        self.me = "mr.yang"
        self.__name = "kivi"        # 私有属性，类外部不可调用

    def __python(self):             # 私有方法，类外部（实例）不可调用
        print "I love python"

    def code(self):
        print "which language do you like"

    @property                       # 通过装饰器@property调用类私有属性
    def name(self):
        return self.__name

if __name__ == "__main__":
    # 种种多态表现，皆因为Python是一种解释型的语言，不需要进行预编译，只在运行时才确定状态
    print length("how are you")
    print length({"lang":"python","book":"itdiffer.com"})

    p = ProtectMe()
    print p.me
#    print p.__name          # 私有属性不能调用
    print p.code()
#    print p.__python          私有方法不可调用
