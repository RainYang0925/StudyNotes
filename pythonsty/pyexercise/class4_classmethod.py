#!/usr/bin/env python
# coding=utf-8

class Foo(object):        #Python 3: class Foo:
    one = 0

    def __init__(self):
        Foo.one = Foo.one + 1

def get_class_attr(cls):        #它引用的对象应该具有属性one
    return cls.one


#类方法 @classmethod
class Foo1(object):
    one = 0

    def __init__(self):
        Foo1.one = Foo1.one + 1

    @classmethod                  #装饰器@classmethod所装饰的方法，其参数cls引用的对象是类对象Foo1
    def get_class_attr(cls):
        return cls.one


if __name__ == "__main__":
    f1 = Foo()
    print "f1:",Foo.one        #Python 3: print("f1:"+str(Foo.one))，下同，从略
    f2 = Foo()
    print "f2:",Foo.one

    print get_class_attr(Foo)   #调用这个函数的时候，就直接将该类对象传给了它,这种写法是应该避免的