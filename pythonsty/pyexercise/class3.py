#!/usr/bin/env python2
# coding=utf-8

# 类属性
class A(object):
    x = 7  # 创建一个类的属性
    # 类属性仅与其所定义的类绑定，并且这种属性，本质上说就是类中的变量
    # 它的值不依赖于任何实例，只是由类中所写的变量赋值语句确定


class Girl(object):
    breast = 90  # 静态变量或者静态数据


class Person(object):
    """
    This is a sample of class.
    1.创建实例对象；
    2.检查是否有——专业的说法：是否实现——__init__()方法。如果没有，则返回实例对象
    3.如果有__init__()，则调用该方法，并且将实例对象作为第一个参数self传递进去
    """

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def color(self, color):
        d = {}
        d[self.name] = color
        return d


class Foo:
    def __init__(self):
        print("I am in init()")


# return 1                    __init()__不能有return／有则return None

class Person1:
    def __init__(self, name, lang="golang", website="www.google.com"):
        '''
        初始化参数
        :param name:
        :param lang:
        :param website:
        '''
        self.name = name
        self.lang = lang
        self.website = website
        self.email = "qiwsir@gmail.com"

#    def get_name(self):
#        return self.name

class B(object):
    y = [1, 2, 3]              #变量引用的是一个可变对象

if __name__ == "__main__":
    print A.x  # A.x是调用类属性的方式
    A.y = 9  # 对类A增加了一个新的属性，并且赋给了值
    print A.y

    #    del A.x
    #    print A.x
    print Girl.breast
    Girl.breast = 40  # 修改当前已有的类属性
    print Girl.breast

    print dir(Girl)
    print Girl.__name__
    print Girl.__doc__
    print Girl.__dict__
    print Girl.__module__
    print Girl.__base__

    #    bar = Foo()
#   print Person1.lang   没有实列化类class Person1 has no attribute 'lang'
    Rain = Person1("yangyu")
    print Rain.lang
    print Rain.website
    print Rain.name

    foo = A()
    print foo.x
    foo.x += 1                  #修改实例foo属性,其本质是该实例foo又建立了一个新的属性
    print foo.x                 #原来的foo.x就被“遮盖了”，只能访问到新的foo.x，它的值是8

    A.x += 1                    #类中变量引用的是不可变数据,实例属性跟着类属性而改变。
    print A.x, foo.x

    print B.y                   #类属性
    bar = B()                   #实例属性
    print bar.y
#当类中变量引用的是可变对象是，类属性和实例属性都能直接修改这个对象，从而影响另一方的值
    bar.y.append(4)
    print bar.y, B.y

    B.y.append("aa")
    print bar.y, B.y
#如果增加一个类属性，相应的也增加了一个实例属性
    A.y = "hello"
    print foo.y

    foo.z = "python"
    print foo.z
#    print A.z                      type object 'A' has no attribute 'z'