#!/usr/bin/python
#-*- coding: utf-8 -*-
# author : KDr2
#

import web
import router 

import feeds
import comments

app = web.application(router.route.urls(),router.route.handlers())

print router.route.urls()
print router.route.handlers()

web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr)
if __name__ == "__main__":
    app.run()



    
