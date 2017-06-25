# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string

from models import Language, Group, Expression
from forms import GroupForm, ExpressionForm, ExpressionGroupForm
from views_examination import start_test_view, show_next_expression


def next_word(request):
    return show_next_expression(request)


def start_test(request, group_id):
    return start_test_view(request, group_id)
