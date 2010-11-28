#-*- coding:utf-8 -*-

import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from kdr2net.lib.base import BaseController, render, Session
from kdr2net.model import Comment
import kdr2net.lib.helpers as h
import simplejson as json


log = logging.getLogger(__name__)

class CommentsController(BaseController):

    def index(self):
        # Return a rendered template
        #return render('/comments.mako')
        # or, return a string
        return 'Hello World'

    def get_comments(self,user_url=""):
        comments=Session.query(Comment).filter_by(target=user_url).order_by(Comment.date)
        if comments.count()==0: return "[]"
        comments_map=map(Comment.dict,comments)
        return json.dumps(comments.count())

    def post_comment(self):
        #if(request.method!="POST"):
        #    abort("404");
        comment=Comment(request.POST)
        try:
            Session.add(comment)
            Session.commit()
            h.sendmail_text(u"killy.draw@gmail.com",u"[kdr2.net]新回复:http://kdr2.net/"+comment.target,str(comment))
            #Title="[kdr2.net] %s left a message on %s" % (comment.author,comment.target)
            #mail_admins(title, comment.content, fail_silently=False)
            return json.dumps([comment.dict()])
        except Exception,e:
            return "ERR %s" % e

