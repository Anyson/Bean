# coding=utf-8 

from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from dajaxice.core import dajaxice_autodiscover, dajaxice_config
#from django.views.generic.base import RedirectView

handler404 = 'schools.views.page_not_found'
handler500 = 'schools.views.page_error'

dajaxice_autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'schools.views.home', name='home'),
    url(r'^index.html$', 'schools.views.home', name='home'),
    url(r'^index/$', 'schools.views.home', name='home'),
    url(r'^school/$', 'schools.views.show_school', name='school'),
    url(r'^article/$', 'schools.views.show_article', name='article'),
    url(r'^search/$', 'schools.views.show_search_result', name='search'),
    #url(r'^favicon\.ico$', RedirectView.as_view(url=settings.STATIC_URL+'/schools/favicon.ico')),
    # url(r'^blog/', include('blog.urls')),
    
    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += patterns('',
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
)
