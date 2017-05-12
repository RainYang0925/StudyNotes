#!/usr/bin/env python
# coding=utf-8

#self 的作用
class Person(object):
    def __init__(self,name):
        self.name = name            #self就是类Person的实例
        print self                  #self.name中的name和初始化函数的参数name没有任何关系
        print type(self)


#类 数据流转

class PersonOne(object):
    def __init__(self,name):
        self.name = name

    def get_name(self):
        return self.name

    def breast(self, n):
        self.breast = n

    def color(self, color):
        print "%s breast is %s" % (self.name, color)

    def how(self):
        print "%s breast is %s" % (self.name, self.breast)


if __name__ == "__main__":

    girl = Person("changlaoshi")
    print girl

    print type (girl)

    girlone = PersonOne('canglaoshi')
    print girlone.breast(90)

    print girlone.color("white")
    print girlone.how()