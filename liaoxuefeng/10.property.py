#!/usr/bin/env python3
# coding: utf-8

class Screen(object):
    __slots__ = ('width', 'height')

    def __init__(self):
        self.width = 0
        self.height = 0

    @property
    def resolution(self):
        return self.width * self.height


# 测试:
if __name__ == '__main__':
    s = Screen()
    s.width = 1024
    s.height = 768
    print('resolution =', s.resolution)
    if s.resolution == 786432:
        print('测试通过!')
    else:
        print('测试失败!')
