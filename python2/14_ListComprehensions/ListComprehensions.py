#coding: utf-8
import os 

print range(1, 11)
print '\n'

print [x * x for x in range(1, 11)]
print '\n'

print [x * x for x in range(1, 11) if x % 2 == 0]
print '\n'

print  [m + n for m in 'ABC' for n in 'XYZ']
print '\n'

print [d for d in os.listdir('../')]
print '\n'

d = {'x': 'A', 'y': 'B', 'z': 'C' }
print d
print '\n'

d = {'x': 'A', 'y': 'B', 'z': 'C' }
print [k + '=' + v for k, v in d.items()]
print '\n'

L = ['Hello', 'World', 'IBM', 'Apple']
print [s.lower() for s in L]