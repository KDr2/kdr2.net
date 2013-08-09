#!/usr/bin/python
#-*- coding: utf-8 -*-
# author : KDr2
#

import os
import re
import web
import json
import datetime

import utils
import router

@router.route(r'/tumblr/feed.json')
class TumblrFeedGetter(object):

    def GET(self):
        tumblr=utils.get_tumblr_rss(max_size=5)
        return json.dumps(tumblr)

