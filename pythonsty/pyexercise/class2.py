#!/usr/bin/env python2
# coding=utf-8

#创建类

class Persion(object):              #类名称首字母大写
    """
    This is a sample of class.
    #BB是继承自类object的新类
    #python 3中，所有的类自然地都是类object的子类，就不用彰显出继承关系
    """
    #类里面的函数->方法，函数（方法）的参数必须包括self参数
    def __init__(self, name):       #__init__()特殊方法，构造函数／初始化函数
        self.name = name            #self的作用，它实质上就是实例对象本身，当你用实例调用方法的时候，由解释器将那个实例传递给方法，
                                    # 所以不需要显示地为这个参数传值

    def get_name(self):
        return self.name

    def color(self, color):
        d = {}
        d[self.name] = color
        return d

#######################################################################
#实例
#类是对象的定义，实例才是真实的物件
#类提供默认行为，是实例的工厂
#######################################################################


if __name__ == "__main__":

    girl = Persion("canglaoshi")        #创建类的实例
    print girl.name
    name = girl.get_name()
    print name
    her_color = girl.color("white")
    print her_color
