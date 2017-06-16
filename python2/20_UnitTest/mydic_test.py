#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 6/15/17 5:33 PM
# @Author  : BluePandaLi 
# @Site    : pandasharp.com
# @File    : uniTest.py
import unittest
from mydict import Dict

class TestDict(unittest.TestCase):

    def setUp(self):
        print 'setUp...'

    def tearDown(self):
        print 'tearDown...'

    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEquals(d.a, 1)
        self.assertEquals(d.b, 'test')
        self.assertTrue(isinstance(d, dict))
        print "test init"

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEquals(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEquals(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):#??
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty

#https://stackoverflow.com/questions/17447268/python-unittest-not-running
#Then unindent that if to the top level (no spaces before it). Otherwise it is part of the code block of the class definition and will be executed before the class is finished (thus no unit tests have been created at this point).
if __name__ == '__main__':
        unittest.main()

#python -m unittest mydict_test
