import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from kdr2net.lib.base import BaseController, render, Session
from kdr2net.model import Comment
import json


log = logging.getLogger(__name__)

class CommentsController(BaseController):

    def index(self):
        # Return a rendered template
        #return render('/comments.mako')
        # or, return a string
        return 'Hello World'

    def get_comments(self,user_url=""):
        comments=Session.query(Comment).filter_by(target=user_url).order_by(Comment.date)
        comments_map=map(Comment.dict,comments)
        return json.dumps(comments_map)

    def post_comment(self):
        #if(request.method!="POST"):
        #    abort("404");
        comment=Comment(request.POST)
        try:
            Session.add(comment)
            Session.commit()
            #title="[kdr2.net] %s left a message on %s" % (comment.author,comment.target)
            #mail_admins(title, comment.content, fail_silently=False)
            return json.dumps([comment.dict()])
        except Exception,e:
            return "ERR %s" % e

