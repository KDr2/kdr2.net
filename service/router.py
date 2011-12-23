#!/usr/bin/python
#-*- coding: utf-8 -*-
# author : KDr2
#

import os
import sys
import glob

__ALL__=['route']

class route(object):

    __URLS__=[]
    
    __HANDLERS__={}
    
    def __init__(self,url):
        self._url=url

    def __call__(self,cls):
        self.__class__.__URLS__.append(self._url)
        self.__class__.__URLS__.append(cls.__name__)
        self.__class__.__HANDLERS__[cls.__name__]=cls
        
    @classmethod
    def urls(cls):
        return tuple(cls.__URLS__)

    @classmethod
    def handlers(cls):
        return cls.__HANDLERS__
    
        
