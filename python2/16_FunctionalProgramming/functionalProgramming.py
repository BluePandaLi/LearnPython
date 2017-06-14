#coding: utf-8
#Higher-order function
import math

print abs(-10)
print abs
print '\n'

f = abs 
print f
print f(-10)
print '\n'

def add(x, y, f):
    return f(x) + f(y)

print add(5,6, abs)
print '\n'

#???
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()

print f1(), f2(), f3()
print '\n'

#???
def count():
     fs = []
     for i in range(1, 4):
         def f(j):
             def g():
                 return j*j
             return g
         fs.append(f(i))
     return fs

f1, f2, f3 = count()

print f1(), f2(), f3()
