#!/usr/bin/env python
# coding=utf-8

"""
寻找素数
先做一个函数，用它来判断某个整数是否是素数。然后循环遍历
"""

import math

def is_prime(n):
    """
    判断一个数是否是素数
    """
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    primes = [i for i in range(2, 101) if is_prime(i)]    #从2开始，因为1显然不是质数
    print primes    #Python 3: print(primes)