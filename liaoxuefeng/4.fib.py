#!/usr/bin/env python3
# coding: utf-8
# 斐波拉契数列

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        # print(a, b)
        print(b)
        a, b = b, a + b
        n = n+1
    return 'done'

# TEST
fib(5)
