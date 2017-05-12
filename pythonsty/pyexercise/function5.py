# --*-- coding:utf-8 --*--
#装饰器，函数——是对象——能够被传递，也能够嵌套
def foo(fun):
    def wrap():
        print "start"        #Python 3用户请自行更换为print()，下同，从略
        fun()
        print "end"
        print fun.__name__
    return wrap

def bar():
    print "I am in bar()"

@foo                  #foo()是装饰器函数，使用@foo来装饰bar()函数。
def bar2():
    print "I am in bar2()"

if __name__ == "__main__":
    f = foo(bar)
    print f()

    print bar2()


    # lambda函数，匿名函数是一个只用一行就能解决问题的函数
    #在lambda后面直接跟变量
    # 变量后面是冒号
    # 冒号后面是表达式，表达式计算结果就是本函数的返回值
    def add(x):
        x += 3
        return x


    number = range(10)
    print number

    new_number = [i+3 for i in number]
    print new_number
    #lambda arg1, arg2, ...argN : expression using arguments
    lam = lambda x:x+3
    print lam(2)
    n2 = []
    for i in number:
        n2.append(lam(i))
    print n2

    #map 基本样式是map(func,seq)
    #unc是一个函数，seq是一个序列对象。
    # 在执行的时候，序列对象中的每个元素，按照从左到右的顺序，
    # 依次被取出来，塞入到func那个函数里面，
    # 并将func的返回值依次存到一个列表中。
    print map(lambda x:x+3,number)
    lst1 = [1, 2, 3, 4, 5]
    lst2 = [6, 7, 8, 9, 0]
    lst3 = [7, 8, 9, 2, 1]
    print map(lambda x, y: x + y, lst1, lst2)
    print map(lambda x,y,z: x+y+z, lst1, lst2, lst3)

    #reduce map是上下运算，reduce是横着逐个元素进行运算
    print reduce(lambda x,y: x+y,[1, 2, 3, 4, 5])

    #filter 过滤器，在Python中，它就是起到了过滤器的作用
    numbers = range(-5, 5)
    print filter(lambda x: x > 0, numbers)


