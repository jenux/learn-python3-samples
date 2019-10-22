#!/bin/python3
# coding: utf-8
# 杨辉三角

def triangles(x):
    if x == None or x <= 0:
        return None
    n = 0
    lastRes = []
    while n < x:
        n = n + 1
        res = []
        for d in range(0, n):
            if d == 0 or d == n-1:
                res.append(1)
            else:
                res.append(lastRes[d] + lastRes[d-1])
        lastRes = res
        yield res

# TEST
print(triangles(10))

for x in triangles(10):
    print(x)

