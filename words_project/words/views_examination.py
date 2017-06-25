# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from random import randint

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.utils.translation import ugettext

from models import Language, Group, Expression
from forms import GroupForm, ExpressionForm
# Create your views_dir here.

"""
Ogolnie jest funkcjonalnosc testow mozemy zrealizowac na kilka sposobow

1. na poczatku za jednym razem wyciagamy liste wszystkied expression id z danej grupy, przechowujemy ja w sesji,
    i na kolejne zadania uzytkownika wybieramy losowo jedno id z listy i zwracamy expression o takim id

2. na kazde zadanie losowac liczbe n z przedzialu <1, expression_query.count()>,
   i zwracac query.exclude(id__in=[list juz wylosowanych n]).ordery_by('id')[n]

3. trzymac w session wszystkie obiekty zwrocone przez query i losowo wybierac kolejno
"""


def init_test(request, group_id):
    # koncepcja jest nastepujaca:
    # przy starcie testu pobieramy liste id ze wszystkich expression z danej grupy
    # taka liste przechowujemy w sesji uzytkownika
    # potem na kazde zadanie nowego slowka wybieramy losowo jedno id z listy i zwracamy takie slowko

    # 1. get expression_ids form given group to test
    expression_query = Expression.objects.filter(groups__id=group_id, groups__user=request.user)

    if not expression_query.exists():
        # return JsonResponse({'error': 'Grupa nie ma zadnych slowek'})
        return {'error': ugettext('the chosen group has no words')}

    count = expression_query.count()

    expression_ids = list(expression_query.values_list('id', flat=True))
    n = randint(0, count - 1)  # moze nie obliczac len, tylko trzymac count na poczatku a potem dekrementowac
    chosen_id = expression_ids.pop(n)
    expression = Expression.objects.get(id=chosen_id)

    # 2. set expression_ids in user session
    request.session['expression_ids'] = expression_ids
    request.session['count'] = count - 1

    # return JsonResponse({'expression': expression})
    return {'expression': expression}


def start_test_view_2(request, group_id):
    result = init_test(request, group_id)
    if 'error' in result:
        return render(request, 'words/group_test.html', {'error': result['error']})

    return render(request, 'words/group_test.html', {'expression': result['expression']})


def start_test_view(request, group_id):
    # koncepcja jest nastepujaca:
    # przy starcie testu pobieramy liste id ze wszystkich expression z danej grupy
    # taka liste przechowujemy w sesji uzytkownika
    # potem na kazde zadanie nowego slowka wybieramy losowo jedno id z listy i zwracamy takie slowko

    # 1. get expression_ids form given group to test
    expression_query = Expression.objects.filter(groups__id=group_id, groups__user=request.user)

    if not expression_query.exists():
        # return JsonResponse({'error': 'Grupa nie ma zadnych slowek'})
        return render(request, 'words/group_test.html', {'error': ugettext('the chosen group has no words')})

    count = expression_query.count()

    expression_ids = list(expression_query.values_list('id', flat=True))
    n = randint(0, count - 1)  # moze nie obliczac len, tylko trzymac count na poczatku a potem dekrementowac
    chosen_id = expression_ids.pop(n)
    expression = Expression.objects.get(id=chosen_id)

    # 2. set expression_ids in user session
    request.session['expression_ids'] = expression_ids
    request.session['count'] = count - 1

    # return JsonResponse({'expression': expression})
    return render(request, 'words/group_test.html', {'expression': expression})


def show_next_expression(request):
    next_expression = get_next_expression(request)
    if next_expression is None:
        return JsonResponse({'end': ugettext('end of test')})
    return JsonResponse({'expression': next_expression.key})


def get_next_expression(request):
    expression_ids = request.session['expression_ids']
    if expression_ids:
        n = randint(0, request.session['count'] - 1)  # moze nie obliczac len, tylko trzymac count na poczatku a potem dekrementowac
        chosen_id = expression_ids.pop(n)

        request.session['expression_ids'] = expression_ids
        request.session['count'] -= 1
        return Expression.objects.get(id=chosen_id)

    return None

