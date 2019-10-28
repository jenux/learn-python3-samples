#!/usr/bin/env python3
# coding: utf-8


def normalize(name):
    def trans(s):
        return s[0:1].upper() + s[1:].lower()

    return list(map(trans, name))

# TEST
print(normalize(['adam', 'LISA', 'barT']))


# 接受一个list并利用reduce()求积
from functools import reduce
def prod(L):
    def fn(x, y):
        return x * y
    return reduce(fn, L)

#print('3 x 5 x 7 x 9 =', prod([3,5,7,9])
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')
