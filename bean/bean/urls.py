# coding=utf-8 

from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from dajaxice.core import dajaxice_autodiscover, dajaxice_config
dajaxice_autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'schools.views.home', name='home'),
    url(r'^index.html$', 'schools.views.home', name='home'),
    url(r'^index/$', 'schools.views.home', name='home'),
    url(r'^school/$', 'schools.views.show_school', name='school'),
    # url(r'^blog/', include('blog.urls')),
    
    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += patterns('',
    url(r'^upload/(?P<path>.*)$','django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
)