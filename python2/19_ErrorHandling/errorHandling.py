#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 6/15/17 2:40 PM
# @Author  : BluePandaLi 
# @Site    : pandasharp.com
# @File    : errorHandling.py

import logging
logging.basicConfig(level=logging.INFO)

#catch
def devide(a, b):
    try:
        print 'try...'
        r = a / b
        print 'result:', r
    except ValueError, e:
        print 'Value Error:', e
    except ZeroDivisionError, e:
        print 'ZeroDivisionError:', e
        logging.exception(e)
    else:
        print 'else'
    finally:
        print  'finally...'
    print 'END'

devide(10, 0)
print '\r'
devide(10, 1)
print '\n'

# raise
class FooError(StandardError):
    pass

def foo(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value: %s' % s)
    return 10 / n

print foo('10')
print '\r'

try:
    print foo('0')
except FooError, e:
    print e
finally:
    print "End"

#print
print "DEBUG MESSAGE"

#assert python -O
try:
    assert False, 'assert error!'
except AssertionError, e:
    print 'Assert error: %s' % e
finally:
    print 'End'
print '\n'

#logging.info()
s = '0'
n = int(s)
logging.info('n = %d' % n)
print 10 / n
