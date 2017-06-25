# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render
from django.utils.translation import ugettext

from words.forms import UserCreationForm


def register_new_user(request):
    user_form = UserCreationForm(request.POST)
    if user_form.is_valid():
        if User.objects.filter(username=user_form.cleaned_data['username']).exists():
            return render(request, 'words/auth/register.html', {'user_form': user_form, 'error': u'Użytkownik o takiej nazwie już istnieje'})

        user = user_form.save(commit=False)
        password = user_form.clean_password2()
        user.set_password(password)
        user.save()
        return render(request, 'words/auth/login.html', {'registered': u'Użytkownik został zarejestrowany! Teraz możesz się zalogować.'})
    else:
        if 'username' in user_form.errors:
            if 'username already exists' in user_form.errors['username'][0]:
                return render(request, 'words/auth/register.html', {'user_form': user_form, 'error': u'Użytkownik o takiej nazwie już istnieje'})
        return render(request, 'words/auth/register.html', {'user_form': UserCreationForm(), 'error': u'Niepoprawne dane'})


def get_register_view(request):
    return render(request, 'words/auth/register.html', {'user_form': UserCreationForm()})


def log_user_in(request):
    user = authenticate(username='john', password='secret')
    if user is not None:
        # A backend authenticated the credentials
        pass
    else:
        pass
        # No backend authenticated the credentials
