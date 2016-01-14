from django.conf.urls import patterns, include, url
from django.contrib import admin
from timeline import views


urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'timeliner.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       # url(r'^$', include('timeline.urls', namespace='timeline')),

                       url(r'^admin/', include(admin.site.urls)),
                       # url(r'^login$', views.login),
                       # url(r'^login/register$', views.register),
                       # url(r'^$', views.index),
                       url(r'', include('timeline.urls', namespace='timeline'))
                       )
