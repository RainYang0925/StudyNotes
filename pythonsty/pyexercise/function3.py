# -*- coding:utf-8 -*-

# 函数参数不确定性,给函数传入多个值

def func(x, *args):
    print x
    result = x
    print args
    for i in args:
        result += i
    return result


# 如果输入的参数个数不确定，其它参数全部通过*arg，以元组的形式由arg收集起
def foo(*args):
    print args


# 如果用**kargs的形式收集值，会得到dict类型的数据，但是，需要在传值的时候说明“键”和“值”
def foo2(**kwargs):
    print kwargs


def foo3(x, y, z, *args, **kwargs):
    print x
    print y
    print args
    print kwargs

def add(x, y):
    return x + y

#参数对应传值，位置对应
def foo4(p1,p2,p3):
    print "p1==>", p1
    print "p2==>", p2
    print "p3==>", p3




if __name__ == '__main__':
    res = func(1, 2, 4, 5, 6)
    print res

    # 结果返回一个元组
    print foo("python")
    print foo(1, 2, 3)
    print foo("love", "me")
    print foo()
    # 结果返回一个字典
    print foo2(a=1, b=2, c=3)

    print foo3(2, "hello", "python")
    print foo3('qiwsir', 2, "python")
    print foo3(1,2,3,4,5,name="qiwsir")

    print add(2,3)
    #元组中元素的个数，要跟函数所要求的变量个数一致
    bars = (2,3)
    print add(*bars)
#    fars = (1,2,3)
#    print add(*fars)

    print foo4("python", 1, ["qiwsir","github","io"])
    #明确指定参数值
    print foo4(p3=3, p1=10, p2=222)
