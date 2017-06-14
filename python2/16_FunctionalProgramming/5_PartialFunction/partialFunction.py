#coding: utf-8
import functools
print int('12345', 8)
print '\n'

int2 = functools.partial(int, base=2)
print int2('1000000')
print int2('1010101')
print '\n'

max2 = functools.partial(max, 10)
print max2(9, 8 , 7)