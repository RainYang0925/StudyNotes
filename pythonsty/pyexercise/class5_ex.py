#!/usr/bin/env python2
# coding=utf-8

#多重继承

class Person(object):
    def eye(self):
        print "tow eyes"

    def breast(self, n):
        print "The breast is:", n

class Girl(object):
    age = 28
    def color(self):
        print "The girl is white"
class HotGirl(Person, Girl):        #多重继承
    pass
#多重继承顺序
class K1(object):        #Python 3: class K1:
    def foo(self):
        print "K1-foo"    #Python 3: print("K1-foo")，下同，从略

class K2(object):        #Python 3: class K2:
    def foo(self):
        print "K2-foo"
    def bar(self):
        print "K2-bar"

class J1(K1, K2):
    pass

class J2(K1, K2):
    def bar(self):
        print "J2-bar"

class C(J1, J2):
    pass


if __name__ == "__main__":
    kong = HotGirl()  #实列化类
    kong.eye()        #继承Person的eye()，breast()
    kong.breast(90)
    kong.color()      #继承类Girl
    print kong.age

    print C.__mro__   #打印类继承顺序
    m = C()
    m.foo()
    m.bar()