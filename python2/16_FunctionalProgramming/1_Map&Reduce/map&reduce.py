#coding utf-8

#map
def f(x):
    return x * x

l = [1, 2, 3, 4, 5, 6]

print map(f, l)
print '\n'

#reduce

def fn(x, y):
    return x * 10 + y

l = [1, 3, 5, 7, 9]

print reduce(fn, l)
print '\n'