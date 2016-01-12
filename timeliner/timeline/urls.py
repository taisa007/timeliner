# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from timeline import views

urlpatterns = patterns('',
                       url(r'^tweets/$', views.tweets, name='tweets'),  # 一覧
                       )
