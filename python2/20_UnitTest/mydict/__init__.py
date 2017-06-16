#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 6/16/17 11:07 AM
# @Author  : BluePandaLi 
# @Site    : pandasharp.com
# @File    : __init__.py.py


class Dict(dict):

    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value