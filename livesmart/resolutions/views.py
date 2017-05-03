# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = 'home.html'


class Login(TemplateView):
    template_name = 'login.html'


class Register(TemplateView):
    template_name = 'register.html'
