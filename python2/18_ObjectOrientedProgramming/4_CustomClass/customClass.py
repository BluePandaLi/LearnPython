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

    def __iter__(self):
        return self.name

print Student('Micael')
print len(Student('abc'))

# for x in Student('abc'):
#     print x