# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from django.db import models
from datetime import date, datetime

# Create your models here.
from words.constants import LANGUAGES, LANGUAGES_DICT


class Language(models.Model):
    name = models.CharField('jezyk', max_length=50, choices=LANGUAGES)

    def __unicode__(self):
        return LANGUAGES_DICT[self.name]


class Group(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField('Nazwa grupy', max_length=50)
    language = models.ForeignKey(Language)
    parent = models.ForeignKey('self', null=True, blank=True)

    # user = models.ForeignKey(User)

    def __unicode__(self):
        return self.name


class Expression(models.Model):
    # group = models.ForeignKey(Group, related_name="deprecated_group")
    groups = models.ManyToManyField(Group)

    key = models.CharField('wyrazenie', max_length=200)
    translation = models.CharField('Translation', max_length=500, null=True, blank=True)
    explanation = models.CharField('Longer explanation', max_length=500, null=True, blank=True)
    example = models.CharField('Example', max_length=500, null=True, blank=True)
    creation_date = models.DateField('Data dodania', null=False, default=date.today)

    image = models.ImageField(upload_to='uploads/%Y/%m/%d/', null=True, blank=True)

    def __unicode__(self):
        return self.key


class Profile(models.Model):

    user = models.OneToOneField(User, null=True)
    languages = models.ManyToManyField(Language)
