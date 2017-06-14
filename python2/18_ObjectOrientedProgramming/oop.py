#!/usr/bin/env python
# -*- coding: utf-8 -*-
import types

class Student(object):

#private
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print '%s: %s' % (self.__name, self.__score)


bart = Student('Bart Simpon', 59)
print bart
print Student
bart.print_score()

print '\n'

class Animal(object):
    def __init__(self):
        self.age = None

    def run(self):
        print 'Animal is running...'

class Dog(Animal):
    def run(self):
        print 'Dog is running...'

class Cat(Animal):
    def run(self):
        print 'Cat is running...'

Dog().run()
Cat().run()
print '\n'

def run_test(*animals):
    for a in animals:
        a.run()

run_test(*[Cat(),Dog(),Animal()])
print '\n'

print 'Dog() is instance of Animal:', isinstance(Dog(), Animal)
print '\'abc\' type is:', type('abc')
print '\'abc\' is StringType:', type('abc') == types.StringType

print type(int)==type(str) == types.TypeType
print type(u'abc')
print type([])
print '\n'

#dir
print dir(Animal())
print '\n'

# attr
a = Animal()
print hasattr(Animal, 'x')
print hasattr(Animal, 'run')
print setattr(a, 'age', 20)
print getattr(a, 'age')
# print getattr(a, 'agex')
print getattr(a, 'agex', 404)
