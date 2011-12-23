#!/usr/bin/python
#-*- coding: utf-8 -*-
# author : KDr2
#


import os
import web
import yaml

from web.contrib.template import render_mako


__CONFIG__={}

def get_config(key,default=None):
    global __CONFIG__
    if not __CONFIG__:
        try:
            cf=os.path.join(os.path.dirname(__file__), 'config.yaml')
            __CONFIG__=yaml.load(file(cf))
        except:
            pass
    return __CONFIG__.get(key,default)

render = render_mako(
    directories=[os.path.join(os.path.dirname(__file__), 'templates')],
    input_encoding='utf-8',
    output_encoding='utf-8')



db=web.database(dbn=get_config('db_dbn','mysql'),
                host=get_config('db_host','127.0.0.1'),
                port=get_config('db_port',3306),
                db=get_config('db_db','test'),
                user=get_config('db_user','root'),
                pw=get_config('db_pw',''))


