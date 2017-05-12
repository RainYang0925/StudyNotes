#!/usr/bin/env python
# coding=utf-8

#方法——跟函数相比，没有本质的不同
class Foo(object):

    #普通方法
    def bar(self):
        print "This is a normal method of class"

class Foo1(object):
    one = 0

    def __init__(self):
        Foo1.one = Foo1.one + 1

    @classmethod                        #类方法
    def get_class_attr(cls):
        return cls.one


def get_class_attr(cls):   #使用类Foo1的one属性，这种写法，使得类和函数的耦合性太强了
    return cls.one


if __name__ == "__main__":

#实例化之后，self和实例f是相同的。通常，我们在类里面使用self，类外面使用f这个实例，两者有分工
    f = Foo()
    print f.bar()
    print Foo.bar(f)
#    print Foo.bar()    unbound method bar() must be called with Foo instance as first argument (got nothing instead)

#当通过类来获取方法的时候，得到的是非绑定方法对象。
#当通过实例获取方法的时候，得到的是绑定方法对象

    f1 = Foo1()
    print "f1:", Foo1.one  # Python 3: print("f1:"+str(Foo.one))，下同，从略
    f2 = Foo1()
    print "f2:", Foo1.one

    print get_class_attr(Foo1)

