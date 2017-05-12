#!/usr/bin/env python
#-*- coding: utf-8 -*-
#函数
# 变量在本质就是一个占位符

a = 2
y = 3 * a + 2

print y
# y = 8
# 修改变量值，y值不变，
a = 3
print y

y = 3 * a + 2
print y
# y = 11

# 定义函数

def add_function(a, b):
    c = a + b
    return c

if __name__ == "__main__":
    result = add_function(2, 3)
    print result




