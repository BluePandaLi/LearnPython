#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 6/14/17 7:58 PM
# @Author  : BluePandaLi 
# @Site    : pandasharp.com
# @File    : customClass.py

class Student(object):
    __slots__ = ('name')
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name

    def __len__(self):
        return  len(self.name)

    def __call__(self, age):
        print 'My name is %s, age %d.' % (self.name, age)

print Student('Micael')
print callable(Student('Micael'))
print Student('Micael')(20)
print len(Student('abc'))

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def next(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100000: # 退出循环的条件
            raise StopIteration();
        return self.a # 返回下一个值

    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

for n in Fib():
    print n


print '\r'
print Fib()[10]
print Fib()[0:11]
print '\n'

class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

print Chain().status.user.timeline.list