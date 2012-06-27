#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author : KDr2


import os
import sys
import glob

def rootdir(subdir=None):
    script=os.path.abspath(os.path.dirname(__file__))
    root=os.path.dirname(script)
    if subdir:
        return os.path.join(root,subdir)
    return root


if __name__=='__main__':
    data_dir=rootdir('data')
    tumblr_feeds='http://n.kdr2.net/rss'
    #os.system("curl %s -H 'Accept-Encoding: gzip' |gunzip - >%s/tumblr_feeds.xml" % (tumblr_feeds,data_dir))
    os.system("curl %s -o %s/tumblr_feeds.xml" % (tumblr_feeds,data_dir))
    

