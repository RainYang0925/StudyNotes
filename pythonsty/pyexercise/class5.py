#!/usr/bin/env python2
# coding=utf-8

#继承
#继承——OOP的三个特征：多态、继承、封装——是类的重要内容。

#################################################################
#继承可以使得子类别具有父类别的各种属性和方法，而不需要再次编写相同的代码。
#在令子类别继承父类别的同时，可以重新定义某些属性，并重写某些方法，
#即覆盖父类别的原有属性和方法，使其获得与父类别不同的功能。
#另外，为子类别追加新的属性和方法也是常见的做法。 （源自维基百科）
###################################################################

#单继承
class P(object):
    pass
class C(P):
    pass

class Person(object):
    def __init__(self, name):
        self.name = name
    def height(self, m):
        h = dict((["height", m],))
        return h
    def breast(self, n):
        b = dict((["breast", n],))
        return b
    @classmethod
    def fun(cls):
        pass

class Girl(Person):
        def get_name(self):
            return self.name
class Girl1(Person):
    def __init__(self):             #重写父类方法，调用时覆盖父类方法
        self.name = "canglaoshi1"
    def get_name(self):
        return self.name

class Girl2(Person):
    def __init__(self, name):
#       Person.__init__(self, name)         #为了能够使用父类的初始化方法，以类方法的方式调用Person.__init__(self, name)
        super(Girl2, self).__init__(name)
        self.real_name = "xioacang"


    def get_name(self):
        return self.name

if __name__ == "__main__":

    cang = Girl("canglaoshi")
    print cang.get_name()  # Python 3: print(cang.get_name())，下同，从略
    print cang.height(160)
    print cang.breast(90)
#如果子类中的方法或属性覆盖了父类（即与父类同名），那么就不在继承父类的该方法或者属性。
    cang1 = Girl1()
    print cang1.get_name()  # Python 3: print(cang.get_name())，下同，从略
    print cang1.height(160)
    print cang1.breast(90)
#子类Girl里面有与父类Person同样名称的方法和属性，也称之为对父类相应部分的重写。
# 重写之后，父类的相应部分不再被继承到子类，没有重写的部分，在子类中依然被继承

    #使用类方法的方式，将父类中被覆盖的方法再次在子类中实现
    cang2 = Girl2("canglaoshi2")
    print cang2.real_name
    print cang2.get_name()
    print cang2.height(160)
    print cang2.breast(90)
