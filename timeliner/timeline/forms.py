# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from timeline.models import User, Tweet


class LoginForm(forms.Form):
    username = forms.CharField(
        label='ユーザ名',
        max_length=60,
        required=True,
        widget=forms.TextInput
    )

    password = forms.CharField(
        label='パスワード',
        max_length=60,
        required=True,
        widget=forms.TextInput
    )


class TweetForm(ModelForm):
    class Meta:
        model = Tweet
        fields = ('content',)
