
import os
import logging
import datetime

from pylons import request, response, session, tmpl_context as c, url, config
from pylons.controllers.util import abort, redirect

from kdr2net.lib.base import BaseController, render

from ConfigParser import ConfigParser

log = logging.getLogger(__name__)

class FeedsController(BaseController):

    def index(self):
        # Return a rendered template
        #return render('/feeds.mako')
        # or, return a string
        return 'Hello World'

    def rss2_0(self):
        item_list=self._changelog()
        print item_list
        c.item_list=item_list
        return render("/rss2_0.mako");


    def _changelog(self):
        site_dir=os.path.dirname(config['here'])
        clfile=os.path.join(site_dir,"source/changelog.ini")
        log.debug(clfile)
        cfg=ConfigParser()
        cfg.read(clfile)
        keys=cfg.sections()
        keys=sorted(keys,reverse=True)
        return map(lambda x:self._section2rssitem(cfg,x),keys)


    def _section2rssitem(self,cfg,section):
        d=datetime.datetime.strptime(section,"%Y-%m-%d %H:%M")
        ret={'pubdate':d.strftime("%a, %d %b %Y %H:%M:%S +0800")}
        keys=['title','link','author','cats','desc','content']
        for key in keys:
            ret[key]=cfg.get(section,key)
        return ret

