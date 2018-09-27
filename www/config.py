#!/usr/bin/env python3
# -*-coding:utf-8 -*-

'''
Configuration
'''

__author__ = 'Jasonjiang'

import config_default

class Dict(dict):
    '''
    Simple dict but support access as x.y style.
    '''
    def __init__(self, names=(), values=(), **kw):
        super(Dict, self).__init__(**kw)
        for k, v in zip(names, values):
            self[k] = v