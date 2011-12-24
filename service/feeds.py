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

from BeautifulSoup import BeautifulSoup as BS


date_re=re.compile(r'^\.\.\s+date\s*:\s*(.*?)\s*$')
info=u"""
<h2>Page(Article) Information / 页面(文章)信息:
  <a class="headerlink" href="#page-article-information" title="Permalink to this headline"></a>
</h2>
<ul class="simple">
  <li>Author : KDr2</li>
  <li>License : |
    <a class="reference external" href="http://creativecommons.org/licenses/by-nc-nd/3.0/deed.en">
       Creative Commons BY-NC-ND 3.0
    </a> |
    <a class="reference external" href="http://creativecommons.org/licenses/by-nc-nd/3.0/deed.zh">
       CC3.0 : 自由转载-非商用-非衍生-保持署名
    </a> |
  </li>
  <li>Hosted on <a class="reference external" href="http://www.dreamhost.com/">DreamHost</a></li>
</ul>
"""


@router.route(r'/feed/rss.*')
class CFeed(object):

    def get_feed_list(self):
        webpy=os.path.abspath(os.path.dirname(__file__))
        feed=os.path.join(os.path.dirname(webpy),"source/update.rst")
        try:
            flist=file(feed).readlines()
            flist=flist[10:]
            flist=[x.strip() for x in flist]
            flist=filter(lambda x:re.compile("^\w.*").match(x),flist)
            return flist
        except:
            return []

    def get_date(self,name):
        webpy=os.path.abspath(os.path.dirname(__file__))
        rst=os.path.join(os.path.dirname(webpy),"source/%s.rst" % name)
        try:
            with open(rst) as f:
                for line in f:
                    m=date_re.match(line)
                    if m:
                        d=m.group(1)
                        d=datetime.datetime.strptime(d,"%Y-%m-%d %H:%M")
                        return datetime.datetime.strftime(d,"%a, %d %b %Y %H:%M:%S +0800")
            return "Sun, 27 Mar 1984 14:17:00 +0800"
        except:
            return "Sun, 23 Jul 1983 23:32:00 +0800"

        
    def get_feed_item(self,name):
        webpy=os.path.abspath(os.path.dirname(__file__))
        page=os.path.join(os.path.dirname(webpy),"build/html/%s.html" % name)
        page=BS(file(page).read())
        item={}
        item['date']=self.get_date(name)
        item['title']=page.html.head.title.string
        item['link']="http://kdr2.net/%s.html" % name
        item['author']='KDr2'
        item['cats']='article'
        art=page.find('div',**{'class':'body'}).first()
        (art.findChildren(recursive=False)[-1]).replaceWith(info)
        (art.findChildren(recursive=False)[0]).clear()
        item['desc']=art
        item['content']=art
        return item
    
    def GET(self):
        web.header('Content-Type', 'text/xml; charset=UTF-8')
        flist=self.get_feed_list()
        feed=map(self.get_feed_item,flist)
        return utils.render.rss(feed=feed)

    
    

