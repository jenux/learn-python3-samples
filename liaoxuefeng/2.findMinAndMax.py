#!/usr/bin/env python3
# coding: utf-8

def findMinAndMax(L):
    min = None
    max = None
    for x in L:
        if min == None or (min != None and x < min):
            min = x
        if max == None or (max != None and x > max):
            max = x
    print(min, max)
    return (min, max)

if findMinAndMax([]) != (None, None):
    print('测试失败1!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败2!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败3!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败4!')
else:
    print('测试成功!')
