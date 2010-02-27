from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render_to_response


def rss2_0(request):
    t=loader.get_template("rss.xml")
    data={"item_list":[]}
    c=Context(data)
    return HttpResponse(t.render(c),content_type="text/xml; charset=UTF-8")

