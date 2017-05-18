#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# 定制类

class C1(object):
    pass

class C2(object):
    pass
# a = C1()，是实例化，创建了一个实例，也是一个赋值语句，将变量a与类C1()建立了引用关系
a = C1()
b = C2()
print type(a)
print type(b)
# isinstance()判断一个对象是否是一个类或者子类的实例
print isinstance(a, C1)
print isinstance(a, C2)

class RoundFloat(object):    # Python 3: class RoundFloat:
    def __init__(self, val):
        assert isinstance(val, float), "value must be a float."
        self.value = round(val, 2)
# 方法__str__()是一个特殊方法。实现这个方法，目的就是能够得到打印的内容
# 这里就是将前面四舍五入保留了两位小数的浮点数，以小数点后有两位小数的形式输出。
    def __str__(self):
        return "{:.2f}".format(self.value)
#__repr__ = __str__ 的含义是在类被调用，即向变量提供__str__()里的内容。
    __repr__ = __str__

# 自定义的分数类
class Fraction1(object):        #Python 3: class Fraction:
    def __init__(self, number, denom=1):
        self.number = number
        self.denom = denom

    def __str__(self):
        return str(self.number) + '/' + str(self.denom)

    __repr__ = __str__


    def __add__(self, other):
        lcm_num = lcm(self.denom, other.denom)
        number_sum = (lcm_num / self.denom * self.number) + (lcm_num / other.denom * other.number)
        return Fraction1(number_sum, lcm_num)

# 最大公约数
def gcd(a, b):
    if not a > b:               # 判断a b 两个数的大小，大的做被除数，小的做除数
        a, b = b, a
    while b != 0:
        remainder = a % b
        a, b = b, remainder
    return a
# 最小公倍数
def lcm(a, b):
    return (a * b) / gcd(a, b)


if __name__ == "__main__":
    r = RoundFloat(2.185)
    print r             # Python 3: print(r)
    print type(r)    # Python 3: print(type(r))

    f = Fraction1(2, 3)
    print f        #Python 3: print(f)


    print gcd(4, 21)
    print lcm(4, 21)