# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from timeline import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name="index"),  # トップ
                       url(r'^login$', views.login, name="login"),  # ログイン
                       url(r'^signup$', views.signup, name="signup"),  # 登録画面
                       url(r'^tweet$', views.tweet, name="tweet"),  # ツイート
                       url(r'^logout', views.logout, name='logout')  # ログアウト
                       )
