# -*- coding: utf-8 -*-
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, render_to_response, redirect, get_object_or_404

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


# ログイン
def login(request):
    data = None
    if request.method == "POST":
        try:
            # DBチェック
            user = User.objects.get(username=request.POST["username"], password=request.POST["password"])

            form = LoginForm(request.POST)
            if form.is_valid():
                # レコードがあったらセッションにユーザ情報書き込む
                request.session['login_session'] = user.id
                return redirect('/')

            data = {'form': form}
        except ObjectDoesNotExist:
            messages.add_message(request, messages.ERROR, 'ユーザ名かパスワードが間違っています。')
            return HttpResponseRedirect('/login')

    return render(request, 'login.html', data)


# 登録画面
def signup(request):
    if request.method == "POST":
        user = User()
        form = LoginForm(request.POST, instance=user)
        user = form.save(commit=False)
        user.save()
        return redirect('/')
    return render_to_response('signup.html',
                              context_instance=RequestContext(request))


def tweet(request):
    tweet = Tweet()
    form = TweetForm(request.POST, instance=tweet)
    if form.is_valid():
        tweet = form.save(commit=False)
        tweet.user_id = 1
        tweet.save()
    return redirect('/')
