#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Student(object):
     __slots__ = ('name', 'age','set_age')  # 用tuple定义允许绑定的属性名称
     pass

print 'dir Student object:', dir(Student())
print 'dir Student class:', dir(Student)
print '\n'

#property
s = Student()
s.name = 'Michael'
print 'dir Student object:', dir(s)
print 'dir Student class:', dir(Student)
print s.name

#medtod
def set_age(self, age):
     self.age = age

from types import MethodType

s.set_age = MethodType(set_age, s, Student)
s.set_age(25)
print s.age
print '\r'

Student.set_age = MethodType(set_age, None, Student)
s2 = Student()
s2.set_age(15)
print s2.age

def set_score(self, score):
     self.score = score

# Student.set_score = MethodType(set_score, None, Student)
# s.set_score(50)