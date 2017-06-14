#coding: utf-8

g = (x * x for x in range(10))

print g
print g.next()
print '\n'

for n in g:
     print n
print '\n'

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1

for x in fib(15):
    print x
print '\n'