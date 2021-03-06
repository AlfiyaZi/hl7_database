from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'hl7.views.index', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?P<num>[0-9]+)/$', 'hl7.views.recordview', name='recordview'),
)
