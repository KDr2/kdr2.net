from django.http import HttpResponse
from kdr2net.comments.models import Comment
import simplejson
import cgi

def get_comments(request,url):
    comments=Comment.objects.filter(target=url)
    comments_map=map(Comment.dict,comments)
    return HttpResponse(simplejson.dumps(comments_map))


def post_comment(request):
    if(request.method!="POST"):
        return HttpResponse("ERR")
    comment=Comment(
        target=request.POST['target'],
        author=request.POST['name'],
        email=request.POST['email'],
        url=request.POST['url'],
        content=cgi.escape(request.POST['content'])
        )
    try:
        comment.save()
        title="[kdr2.net] %s left a message on %s" % (comment.author,comment.target)
        mail_admins(title, comment.content, fail_silently=True)
        return HttpResponse(simplejson.dumps([comment.dict()]))
    except:
        return HttpResponse("ERR")
