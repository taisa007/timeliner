# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response, redirect

# Create your views here.
from django.template.context import RequestContext
from timeline.forms import LoginForm, TweetForm
from timeline.models import Tweet, User


# トップ
def index(request):
    tweets = Tweet.objects.all()
    return render_to_response('index.html',
                              {'tweets': tweets},
                              context_instance=RequestContext(request))


# ログイン画面
def login(request):
    return render_to_response('login.html',
                              context_instance=RequestContext(request))


# ログイン
def login_register(request):

    # DBチェック

    # レコードがあったらセッションにユーザ情報書き込む
    request.session['login_session'] = 'user'

    return redirect('/')


# 登録画面
def signup(request):
    return render_to_response('signup.html',
                              context_instance=RequestContext(request))


# 登録処理
def signup_register(request):
    user = User()
    form = LoginForm(request.POST, instance=user)
    user = form.save(commit=False)
    user.save()
    return redirect('/')


def tweet(request):
    tweet = Tweet()
    form = TweetForm(request.POST, instance=tweet)
    if form.is_valid():
        tweet = form.save(commit=False)
        tweet.user_id = 1
        tweet.save()

    return redirect('/')
