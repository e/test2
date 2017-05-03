# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import TemplateView
from resolutions.models import Resolution


class Home(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        user = self.request.user
        if user.is_authenticated:
            resolutions = Resolution.objects.filter(user=self.request.user)
            return {'resolutions': resolutions}


class Login(TemplateView):
    template_name = 'login.html'


class Register(TemplateView):
    template_name = 'register.html'
