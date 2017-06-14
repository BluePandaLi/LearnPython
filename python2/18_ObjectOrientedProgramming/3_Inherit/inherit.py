#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 6/14/17 7:46 PM
# @Author  : BluePandaLi 
# @Site    : pandasharp.com
# @File    : inherit.py

class TCP():
    def print_self(self):
        print "TCP"

class UDPMixin():
    def print_self(self):
        print "UDP"

class NetWork(TCP, UDPMixin):
    pass

NetWork().print_self()