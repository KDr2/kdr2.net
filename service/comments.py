#!/usr/bin/python
#-*- coding: utf-8 -*-
# author : KDr2
#

import web
import cgi
import json
import base64
import datetime

import utils
import router
import email_sender

def format_comment(cmt):
    ret={}
    keys=['id','parent_id','author','url','content']
    for k in keys:
        v=cmt.get(k,"")
        if isinstance(v,(str,unicode)):v=cgi.escape(v)
        ret[k]=v
    #endfor
    date=cmt.get('date')
    ret['date']=date.strftime("%D %H:%m")
    return ret

#@router.route(r'^/(.*)')
class x(object):

    def GET(self,target):
        return "URL:"+target

    
@router.route(r'/comments/get/(.*)')
class CommentsGetter(object):

    def GET(self,target):
        data={"target":target}
        comments=utils.db.select('comments',data,where='target=$target')
        comments=map(format_comment,comments)
        return json.dumps(comments)


@router.route(r'/comments/post')
class CommentsPoster(object):

    def POST(self):
        #return web.notfound("Sorry")

        comments = web.input()
        if not hasattr(comments,'target') or \
                not hasattr(comments,'content') or\
                not hasattr(comments,'name'):
            return web.internalerror("Bad Post.")
        data={'date':web.SQLLiteral("NOW()")}
        #date=datetime.datetime.now()
        data['parent_id']=comments.get('parent_id',0)
        data['target']=comments.get('target','about.html')
        data['author']=comments.get('name','anonym')
        data['url']=comments.get('url','http://kdr2.net')
        data['email']=comments.get('email','')
        data['content']=comments.get('content','nothing')
        sequence_id = utils.db.insert('comments', **data)
        data['id']=sequence_id
        data['date']=datetime.datetime.now()
        try:
            r=base64.decodestring('a2lsbHkuZHJhd0BnbWFpbC5jb20=\n')
            subject=u'[KDr2.net]: New Comment from [%s]' % data['author']
            content=u'Comment Content:\n\n%s\n' % data['content']
            email_sender.sendmail_text(r,subject,content)
        except:
            pass
        return json.dumps([format_comment(data)])



    
