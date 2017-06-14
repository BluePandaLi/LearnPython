#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 6/14/17 7:39 PM
# @Author  : BluePandaLi 
# @Site    : pandasharp.com
# @File    : property.py

class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


s = Student()
s.score = 20
print s.score

s.score = "abc"