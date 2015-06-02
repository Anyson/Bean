# coding=utf-8 

from django.conf.urls import patterns, include, url
from django.contrib import admin
from bean import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bean.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    url(r'^upload/(?P<path>.*)$','django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
)
