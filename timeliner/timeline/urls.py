# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from timeline import views

urlpatterns = patterns('',
                       url(r'^$', views.index),  # トップ
                       url(r'^login$', views.login),  # ログイン
                       url(r'^login/register$', views.login_register),  # ログイン

                       url(r'^signup$', views.signup),  # 登録画面
                       url(r'^signup/register$', views.signup_register),  # 新規登録処理

                       url(r'^tweet$', views.tweet),  # ツイート
                       )
