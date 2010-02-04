from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

import kdr2net.comments.views

urlpatterns = patterns(
    '',

    # Example:
        # (r'^comments/', include('comments.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
        # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    (r'^admin/', include(admin.site.urls)),
    (r'service/post_comment/',kdr2net.comments.views.post_comment),
    (r'service/get_comments/(.*)',kdr2net.comments.views.get_comments),
    (r'service/static/(?P<path>.*)$', 'django.views.static.serve',
     {'document_root': settings.MEDIA_ROOT}),
    )
