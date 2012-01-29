#!/usr/bin/python
#-*- coding: utf-8 -*-
# author : KDr2
#

import web
import router 

import feeds
import comments
import tumblr

import locale

locale.setlocale(locale.LC_ALL,"en_US.UTF-8")

app = web.application(router.route.urls(),router.route.handlers())

web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr)

if __name__ == "__main__":
    app.run()

    
