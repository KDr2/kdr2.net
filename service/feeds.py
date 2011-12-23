#!/usr/bin/python
#-*- coding: utf-8 -*-
# author : KDr2
#

import os
import json

import utils
import router


@router.route(r'/feed/rss.*')
class Feed(object):

    def GET(self):
        webpy=os.path.abspath(os.path.dirname(__file__))
        feed=os.path.join(os.path.dirname(webpy),"source/changelog.js")
        feed=json.load(file(feed))
        return utils.render.rss(feed=feed)
    

