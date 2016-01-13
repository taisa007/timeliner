# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response, redirect

# Create your views here.
from django.template.context import RequestContext
from timeline.forms import LoginForm
from timeline.models import Tweet, User


def index(request):
    tweets = Tweet.objects.all()
    return render_to_response('tweets.html',
                              {'tweets': tweets},
                              context_instance=RequestContext(request)
                              )


# ログイン
def login(request):
    return render_to_response('login.html',
                              context_instance=RequestContext(request))


def register(request):
    user = User()
    form = LoginForm(request.POST, instance=user)
    user = form.save(commit=False)
    user.save()
    return redirect('/')


def tweets(request):
    tweets = Tweet.objects.all()
    return render_to_response('tweets.html',
                              {'tweets': tweets},
                              context_instance=RequestContext(request)
                              )
