#!/usr/bin/env python
# -*- coding: utf-8 -*-
' a test module '
from __future__ import division
__author__ = 'BluePandaLi'

import sys

try:
    import cStringIO as StringIO
except ImportError:
    import StringIO

def test():
    args = sys.argv
    if len(args)==1:
        print 'Hello, world!'
    elif len(args)==2:
        print 'Hello, %s!' % args[1]
    else:
        print 'Too many arguments!'

if __name__=='__main__':
    test()


def _private_print_name(name):
    return 'Hello', '%s' % name

def print_name(name):
    return _private_print_name(name)