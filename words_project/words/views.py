# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.template.loader import render_to_string
from django.db import transaction

from models import Language, Group, Expression
from forms import GroupForm, ExpressionForm, ExpressionGroupForm


# Create your views here.


def index(request, error=None):
    # print('language: ' + str(request.LANGUAGE_CODE))
    languages = Language.objects.all()
    groups = Group.objects.filter(user=request.user)
    expression_form = ExpressionForm(user=request.user)
    return render(request, 'words/index.html', {'languages': languages, 'group_form': GroupForm(user=request.user),
                                                'groups': groups, 'expression_form': expression_form})


def groups_view(request):
    groups = Group.objects.filter(user=request.user)
    return render(request, 'words/all_groups.html', {'groups': groups})


def get_groups_for_lang(request, language):
    groups = Group.objects.filter(user=request.user, lagnuage=language)
    expression_form = ExpressionForm(user=request.user)
    return render(request, 'words/groups.html', {'groups': groups, 'expression_form': expression_form})


def add_new_group(request):
    if request.method == 'POST':
        form = GroupForm(request.POST, user=request.user)
        if form.is_valid():
            new_group = form.save(commit=False)
            new_group.user = request.user
            if Group.objects.filter(user=request.user, name=new_group.name).exists():
                # error, cannot duplicate name for the same user
                return index(request)

            new_group.save()
    return index(request)


@transaction.atomic
def add_new_expression(request):
    if request.method == 'POST':
        form = ExpressionForm(request.POST, user=request.user)
        if form.is_valid():
            expression = form.save(commit=False)
            if Expression.objects.filter(key=expression.key).exists():
                # error, cannot duplicate name for the same user
                return index(request)
            expression.save()
            form.save_m2m()
        else:
            print('nie poszla walidacja')
    else:
        print('method not post!')
    return index(request)


def see_group(request, group_id):
    group = Group.objects.get(id=group_id)
    expressions = Expression.objects.filter(groups=group)
    expression_form = ExpressionGroupForm(group=group)
    add_word_form = render_to_string('words/add_new_word.html', {'expression_form': expression_form})
    return render(request, 'words/group_details.html', {'group': group, 'expressions': expressions,
                                                        'add_word_form': add_word_form})

