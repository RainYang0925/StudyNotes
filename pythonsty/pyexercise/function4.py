# -*-coding: utf-8 -*-
#函数递归
#在Python中，递归要慎重使用。
# 在一般情况下，递归是能够被迭代或者循环替代的，而且后者的效率常常比递归要高
def fib(n):
    """
    This is Fibonacci by Recursion.
    """
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
"""
the better Fibonacci
"""
meno = {0:0, 1:1}

def fib2(n):
    if not n in meno:
        meno[n] = fib(n-1) + fib(n-2)
    return meno[n]
#函数参数中传递函数，函数也是对象可传递给参数
#Python中默认类型的对象以引用的方式传入函数——也可以传入以后要学习过的自定义类型的对象引用
#example_1
def bar():
    print "i am in bar()"
def foo3(func):
    func()

#example_2:字符串转换函数
def convert(func, seq):
    return [func(i) for i in seq]
def num(n):
    if n%2 == 0:
        return n**n
    else:
        return n*n

#嵌套函数
def foo4():
    def bar():
        print "bar() is running"        #Python 3用户请修改为print()函数，下同，从略

    bar()                               #显示调用，作用域仅在foo4()函数块内
    print "foo4() is running"

def foo5():
    a = 1
    def bar():
        b = a + 1
        print "b=",b    #Python 3的用户请使用print()
    bar()
    print "a=",a

def maker(n):
    def action(x):
        return x ** n
    return action       #return action返回的是action()函数对象

if __name__ == "__main__":
    f = fib(10)
    print f    #Python 3: print(f)
    print fib2(10)

    print foo3(bar)

    myseq = (111, 3.14, -9.21)
    r = convert(str, myseq)
    print r

    mynum = (2,3,4)
    print convert(num,myseq)

    print foo4()

    f = maker(2) #f所引用的对象是一个函数对象——action()函数对象，print f就是打印这个函数对象的信息
    print f
    m = f(3)
    print m