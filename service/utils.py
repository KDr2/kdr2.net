#!/usr/bin/python
#-*- coding: utf-8 -*-
# author : KDr2
#


import os
import web
import yaml
import urllib2

from HTMLParser import HTMLParser
from web.contrib.template import render_mako
from BeautifulSoup import BeautifulSoup as BS


__CONFIG__={}

def rootdir(subdir=None):
    sd=os.path.abspath(os.path.dirname(__file__))
    root=os.path.dirname(sd)
    if subdir:
        return os.path.join(root,subdir)
    return root


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



def get_tumblr_rss(max_size=None):
    try:
        """
        #f=urllib2.urlopen('http://n.kdr2.net/rss')
        opener = urllib2.build_opener()
        opener.addheaders = [
            ('User-Agent','Mozilla/5.0'),
            ('Cache-Control','no-cache'),
            ]
        f=opener.open('http://n.kdr2.net/rss')
        xml=f.read()
        """
        xml=file(rootdir("data/tumblr_feeds.xml")).read()
        rss=BS(xml)
        items=rss.channel.findAll('item')
        if max_size:items=items[:max_size]
        ret=[]
        for item in items:
            i={'date': item.pubdate.text}
            i['title']=item.title.text
            i['link']=item.guid.text
            i['author']='KDr2'
            i['cats']='tumblr'
            art=item.description.text
            art=HTMLParser.unescape.__func__(HTMLParser,art)
            i['desc']=art
            i['content']=art
            ret.append(i)
        #endfor
        return ret
    except:
        return []


    
