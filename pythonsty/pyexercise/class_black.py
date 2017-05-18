#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# 优化内存的 __slots__

class Spring(object):
    __slots__ = ("tree", "flower")


print dir(Spring)

print Spring.__slots__

t = Spring()  # 创建实例

print t.__slots__

Spring.tree = "liushu"  # 通过类给属性符值


# t.tree = "guangyulan" 不能通实例修改属性AttributeError: 'Spring' object attribute 'tree' is read-only
# 不管是实例还是类，都用__dict__来存储属性和方法，
# 可以笼统地把属性和方法称为成员或者特性，一句话概括，就是__dict__存储对象成员
# 属性拦截
class A(object):
    '''
    __setattr__(self, name,value)：如果要给name赋值，就调用这个方法。
    __getattr__(self, name)：如果name被访问，同时它不存在的时候，此方法被调用。
    __getattribute__(self, name)：当name被访问时自动被调用（注意：这个仅能用于新式类），无论name是否存在，都要被调用。
    __delattr__(self, name)：如果要删除name，这个方法就被调用.
    '''

    def __getattr__(self, name):
        print "You use getattr"

    def __setattr__(self, name, value):
        print "You use setattr"
        self.__dict__[name] = value


a = A()  # 实例a
print a.x  # 访问a.x实例属性, a.x不存在。调用了__getattr__，即所谓“拦截成员”。

a.x = 7  # 给对象的属性赋值时候，调用了__setattr__(self, name, value)方法
print a.x


class B(object):
    def __getattribute__(self, name):
        print "you are useing getattribute"
        return object.__getattribute__(self, name)

b = B()
# print b.y           # 访问不存在的成员,已经被__getattribute__拦截了

b.y = 8
print b.y

print "==============================================================================="

class Rectangle(object):
    '''
    study __getattr__ and __setattr__
    the width and length of Rectangle
    '''
    def __init__(self):
        self.width = 0
        self.length = 0

    def setSize(self, size):
        self.width, self.length = size

    def getSize(self):
        return self.width, self.length

    size = property(getSize, setSize)

class NewRectangle(object):
    def __init__(self):
        self.width = 0
        self.length = 0

    def __setattr__(self, key, value):
        if key == "size":
            self.length, self.width = value
        else:
            self.__dict__[key] = value

    def __getattr__(self, item):
        if item == "size":
            return self.length, self.width
        else:
            raise AttributeError
if __name__ == "__main__":
    r = Rectangle()
    r.width = 3
    r.length = 4
    print r.size
    r.size = 30, 40
    print r.width
    print r.length

    print "==============================================================================="

    r1 = NewRectangle()
    r1.width = 3
    r1.length = 4
    print r1.size
    r1.size = 30, 40
    print r1.width
    print r1.length