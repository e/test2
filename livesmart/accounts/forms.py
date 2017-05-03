# -*- coding: utf-8 -*-
from django import forms
from .models import User


class RegistrationForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['email', 'date_of_birth', 'first_name', 'last_name']
