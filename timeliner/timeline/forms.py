# -*- coding: utf-8 -*-
from django.forms import ModelForm
from timeline.models import User


class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
