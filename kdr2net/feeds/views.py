#!/usr/bin/python
#author : KDr2

import os
import datetime

from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render_to_response
from ConfigParser import ConfigParser

def rss2_0(request):
    t=loader.get_template("rss.xml")
    item_list=_changelog()
    data={"item_list":item_list}
    c=Context(data)
    return HttpResponse(t.render(c),content_type="text/xml; charset=UTF-8")


def _changelog():
    feeds_app_dir=os.path.dirname(os.path.abspath(__file__))
    site_dir=os.path.dirname(os.path.dirname(feeds_app_dir))
    clfile=os.path.join(site_dir,"source/changelog.ini")
    cfg=ConfigParser()
    cfg.read(clfile)
    keys=cfg.sections()
    keys=sorted(keys,reverse=True)
    return map(lambda x:_section2rssitem(cfg,x),keys)


def _section2rssitem(cfg,section):
    d=datetime.datetime.strptime(section,"%Y-%m-%d %H:%M")
    ret={'pubdate':d.strftime("%a, %d %b %Y %H:%M:%S +0800")}
    keys=['title','link','author','cats','desc','content']
    for key in keys:
        ret[key]=cfg.get(section,key)
    return ret
