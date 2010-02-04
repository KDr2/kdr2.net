from django.db import models
from django.contrib import admin

import datetime

# Create your models here.

class Comment(models.Model):
    target=models.CharField(max_length=60)
    date=models.DateTimeField(default=datetime.datetime.now)
    author=models.CharField(max_length=12)
    email=models.CharField(max_length=30)
    url=models.URLField(default="#")
    content=models.TextField(blank=False)

    def __unicode__(self):
        return u"%s said: %s" % (self.author,self.content)

    def dict(self):
        return {
            'target':self.target,
            'date':self.date.strftime("%D %H:%m"),
            'author':self.author,
            'url':self.url,
            'content':self.content
            }

class CommentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Comment,CommentAdmin)

