#!/usr/bin/python
#-*- coding: utf-8 -*-
# author : KDr2
#


import os
import web

from web.contrib.template import render_mako


render = render_mako(
    directories=[os.path.join(os.path.dirname(__file__), 'templates')],
    input_encoding='utf-8',
    output_encoding='utf-8')



db=web.database(dbn='mysql',
                host="127.0.0.1",
                port=3306,
                db='kdr2_net_dev',
                user='root',
                pw="")


