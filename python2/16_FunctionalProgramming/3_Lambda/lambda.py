#coding: utf-8

def f(x):
    return x * x

print map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print '\n'

def build(x, y):
    return lambda: x * x + y * y

print build(1, 2)()