# -*- coding: utf-8 -*-
from django.forms import ModelForm
from timeline.models import User, Tweet


class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')


class TweetForm(ModelForm):
    class Meta:
        model = Tweet
        fields = ('content',)
